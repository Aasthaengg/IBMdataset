n = int(input())
a = list(map(int, input().split()))
b=0
x=0
for i in range(n):
  if a[i]%2==0:
    x+=1
    if a[i]%3==0 or a[i]%5==0:
      b+=1
print('APPROVED' if b==x else 'DENIED')