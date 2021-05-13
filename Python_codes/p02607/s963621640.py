n=int(input())
a=list(map(int, input().split()))
count = 0
for i in range(1,n+1,2):
  #print(i)
  if a[i-1] % 2 == 1:
    count += 1
print(count)