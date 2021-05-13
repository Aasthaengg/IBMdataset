ans=0
n=int(input())
li=list(map(int,input().split()))
for i in range(len(li)-2):
  if sorted(li[i:i+3])[1]==li[i+1]:
    ans+=1
print(ans)