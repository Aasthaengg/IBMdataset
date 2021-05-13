N=int(input())
A=list(map(int,input().split()))
a=[]
b=[]
for i in A:
    if i%2==0:
        a.append(i)
for n in a:
    if n%3==0 or n%5==0:
        b.append(n)
if len(a)==len(b):
    print('APPROVED')
else:
    print('DENIED')