n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

cnt=0

for i in range(n):
  taoshita=min(A[i],B[i])
  #print(taoshita)
  a=min(A[i+1],B[i]-taoshita)
  #print(a)
  A[i+1]-=a
  cnt+=(taoshita+a)

print(cnt)