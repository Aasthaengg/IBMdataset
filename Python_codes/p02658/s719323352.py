import sys
n=int(input())
a=list(map(int,input().split()))

if 0 in a:
    print('0')
    sys.exit()

c=1

for i in range(n):
    c*=a[i]
    if c>10**18:
        print('-1')
        sys.exit()
    else:
        continue

print(c)