a,b = map(int, input().split())
summ = 0

for i in range(1,b-a+1):
  summ=summ+i
print(summ-b)