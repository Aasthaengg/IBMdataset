N=int(input())
s=input()
t=input()
ans=2*N
for i in range(N):
  A=s[:i]+t
  if A[:N]==s:
    ans=N+i
    break
print(ans)
