import sys

S = set(input())
alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in alpha:
    if not i in S:
        print(i)
        sys.exit()
print('None')

