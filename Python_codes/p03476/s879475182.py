import itertools
n=int(input())
d=[list(map(int,input().split())) for i in range(n)]

sosuu=[1 for i in range(10**5+1)]
#sosuuのindexの値が1の時素数とする。
sosuu[0]=0
sosuu[1]=0
for i in range(2,int((10**5+1)**0.5)+1):
  if sosuu[i]==0:continue
  elif sosuu[i]==1:
    for j in range(2*i,10**5+1,i):
      sosuu[j]=0
like_n=[]
like_n+=sosuu
#奇数なので、2を削除。
like_n[2]=0
for i in range(3,10**5+1):
  if sosuu[i]==0:continue
  elif sosuu[i]==1 and sosuu[(i+1)//2]==0:
    like_n[i]=0
ans= list(itertools.accumulate(like_n))
for ans_d in d:
  print(ans[ans_d[1]]-ans[ans_d[0]-1])

