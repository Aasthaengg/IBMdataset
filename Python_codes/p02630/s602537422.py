n=int(input())
a = list(map(int,input().split()))
q=int(input())
bc = [list(map(int, input().split())) for l in range(q)]
cnt=[0]*100001
Sum=0
for i in range(n):
  cnt[a[i]]+=1
  Sum+=a[i]
for i in range(q):
  Sum+=(bc[i][1]-bc[i][0])*cnt[bc[i][0]]                           
  cnt[bc[i][1]]+=cnt[bc[i][0]]
  cnt[bc[i][0]]=0
  print(Sum)