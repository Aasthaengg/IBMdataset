n,k = map(int,input().split())
p = [0]*n
a = []
ans = 0
for i in range (k):
  a = []
  d = input()
  a = list(map(int,input().split()))
  for j in a:
    p[j-1] +=1
  
for i in p:
  if i == 0:
    ans +=1
print(ans)