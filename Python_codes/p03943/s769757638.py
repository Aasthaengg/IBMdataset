import sys
l = list(map(int,input().split()))

for i in range(3):
    if l[i] == sum(l[:i]+l[i+1:]):
        print('Yes')
        sys.exit()
print('No')
