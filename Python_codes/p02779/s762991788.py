N=int(input())
A=list(map(int,input().split()))
dic={}
for i in range(N):
  if(A[i] not in dic):
    dic[A[i]]=1
  else:
    print("NO")
    exit()
print("YES")