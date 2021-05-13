N = int(input())
List = list(map(int,input().split()))

l = 10**6

for i in List:
  k=0
  while i%2 == 0:
    i/=2
    if i==0: break
    k+=1
    
  l = min(k,l)

print(l)