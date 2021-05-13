N = int(input())
row = list(map(int, input().strip().split()))
count=0
for i in range(0,N,2):
  if row[i]%2==1:
    count+=1
print(count)
