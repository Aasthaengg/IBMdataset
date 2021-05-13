n=int(input())
A=list(map(lambda x: int(x)-1,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

ans = 0
last = A[0]
ans += B[last]
#print(ans)
for a in A[1:]:
  if last + 1 == a:
    ans += C[last]
  ans += B[a]
  last = a
  #print(ans,a,B[a],C[a])
print(ans)