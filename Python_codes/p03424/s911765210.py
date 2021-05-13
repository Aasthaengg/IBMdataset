n=int(input())
s=input().split()

b=1
for i in s:
    if i=='Y':
       b=0

if b==0:
    print('Four')
else:
    print('Three')       