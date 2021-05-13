n=int(input())
s=input().split()

x=set(s)
if len(x)==3:
    print('Three')
else:
    print('Four')