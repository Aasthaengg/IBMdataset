N=int(input())
A=[int(input()) for _ in range(N)]
A.sort()
A.append(0)
ans=0
i=0
j=0
while i<N:
  b=A[i]
  c=0
  while b==A[i] and i<N:
    c+=1
    i+=1
  ans+=(c%2)
print(ans)