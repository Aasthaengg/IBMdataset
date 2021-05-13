n=int(input())
lis=list(input().split())
ans=0
for i in range(n):
  if lis[i] == "Y":
    ans=1
print(["Three","Four"][ans])
