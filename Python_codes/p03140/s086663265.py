# 2019/12/5

n=int(input())
a=list(input())
b=list(input())
c=list(input())

cnt=0
for aa,bb,cc in zip(a,b,c):
    tmp=set([aa,bb,cc])
    cnt+=len(tmp)-1
print(cnt)