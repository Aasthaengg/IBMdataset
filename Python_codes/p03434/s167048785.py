n = int(input())
a = list(map(int, input().split()))

al = 0
bo = 0
a = sorted(a)
for i in range(n):
  if i%2==0:
    al += a[n-1-i]
  else:
    bo += a[n-1-i]
    
print(al-bo)