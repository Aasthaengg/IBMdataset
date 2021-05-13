N=int(input())
L=list(map(int,input().split()))
key=0
for i in L:
  if i%2==0:
    key+=1
ans=3**N-2**key
print(ans)