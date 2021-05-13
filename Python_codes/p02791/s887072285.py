n=int(input())
p=list(map(int,input().split()))

count = 1
pos = p[0]
for i in range(n-1):
  if pos > p[i+1]:
    count += 1
    pos = p[i+1]
print(count)