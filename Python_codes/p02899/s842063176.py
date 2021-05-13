N=int(input())
A=list(map(int,input().split()))
B=[1]*N
for x in range(N):
  B[A[x]-1]+=x
for y in B:
  print(y,end="")
  if y!=B[N-1]:
    print(" ",end="")
print("\n")