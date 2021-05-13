A,B,C,K=map(int,input().split())

if K%2:
  ans=B-A
else:
  ans=A-B
print(ans if abs(ans)<=10**18 else "Unfair")