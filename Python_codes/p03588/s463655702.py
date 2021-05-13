N=int(input())
dic=dict()
for _ in range(N):
  a,b=map(int,input().split())
  dic[a]=b

dic=sorted(dic.items(),key=lambda x:x[0])

ans= dic[-1][0] + dic[-1][1]
print(ans)