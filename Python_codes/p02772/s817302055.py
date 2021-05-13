n = int(input())
a = list(map(int, input().split()))
b=0
for i in range(n):
  if a[i]%2==0 and a[i]%3!=0 and a[i]%5!=0:
      b+=1
print('APPROVED' if b==0 else 'DENIED')