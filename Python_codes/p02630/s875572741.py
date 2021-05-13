n=int(input())
a=list(map(int,input().split()))
q=int(input())
b=[0]*q
c=[0]*q
for i in range(q):
  b[i],c[i]=map(int,input().split())

s=sum(a)

#このコードはO(10**10)になる可能性があり、重すぎる
"""
for i in range(q):
  while b[i] in a:
    s+=c[i]-b[i]
    a.remove(b[i])
    a.append(c[i])
  print(s)
"""

cnt_list=[0]*(10**5+1)
for i in range(n):
  cnt_list[a[i]]+=1

for i in range(q):
  s+=(c[i]-b[i])*cnt_list[b[i]]
  cnt_list[c[i]]+=cnt_list[b[i]]
  cnt_list[b[i]]=0
  print(s)