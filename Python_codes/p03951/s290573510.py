import sys
input=sys.stdin.readline

n=int(input())
s=input().rstrip()
t=input().rstrip()

for i in range(n+1):
    check=True
    for j in range(n-i):
        if s[i+j]!=t[j]:
            check=False

    if check:
        ans=i+n
        print(ans)
        sys.exit()