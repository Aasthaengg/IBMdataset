import sys

s = input()
k = int(input())

for n in s[:k]:
    if int(n) > 1:
        print(n)
        sys.exit()
print(1)