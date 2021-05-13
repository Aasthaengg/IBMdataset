wari = 10**9 + 7
n = int(input())
count = 1
for i in  range(1,n+1):
   count *= i
   count %= wari
print(count)