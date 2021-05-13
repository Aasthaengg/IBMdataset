import sys
sys.setrecursionlimit(10**6)

x=int(input())
a=int(input())
b=int(input())

ans=x-a
ans=ans%b
print(ans)