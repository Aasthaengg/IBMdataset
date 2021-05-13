#累積和的な

n,q = map(int,input().split())
s = input() + 'A' 
li = [0]*(n+1)

for i in range(n):
  li[i+1] = li[i] + (1 if s[i] + s[i+1] == 'AC' else 0)
  

for j in range(q):
  l,r = map(int,input().split())
  print(li[r-1] - li[l-1])