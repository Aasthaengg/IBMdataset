N,k=map(int,input().split())
hako=list(map(int,input().split()))
hako.sort(reverse=True)
fin=0
for i in range(k):
  fin=fin+hako.pop()
print(fin)