N=int(input())
A=input()
B=input()
C=input()
ans=0
for i in range(N):
  X=[0]*26
  X[ord(A[i])-ord('a')]+=1
  X[ord(B[i])-ord('a')]+=1
  X[ord(C[i])-ord('a')]+=1
  X.sort()
  ans+=3-X[25]
print(ans)