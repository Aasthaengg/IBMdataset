N = int(input())
AAA = map(int,input().split())
AA = list(AAA)
count = 0
for i in range(len(AA)):
  a = AA[i]
  if AA[a-1] == i+1:
    count +=1
print(int(count/2))