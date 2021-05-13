b=list(map(int,input().split()))
n=int(input())

ans=max(b)*2**n+sum(b)-max(b)
print(ans)