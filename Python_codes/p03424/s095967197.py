a=int(input())
b=list(map(str,input().split()))
if len(set(b))==3:
    print('Three')
else:
    print('Four')