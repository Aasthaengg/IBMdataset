K,N= map(int, input().split())
x = list(map(int, input().split()))
x.append(K+x[0])
sabun=[]
for i in range(N):
  sabun.append(x[i+1]-x[i])
newsabun=sorted(sabun)[::-1]
print(K-newsabun[0])