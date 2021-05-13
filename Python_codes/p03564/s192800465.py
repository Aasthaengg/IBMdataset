N,K=int(input()),int(input())
num=1
for i in range(N):
  num=min(num*2,num+K)
print(num)