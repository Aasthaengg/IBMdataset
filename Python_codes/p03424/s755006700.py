n=int(input())
s=list(map(str,input().split()))
if len(set(s))==4:
    print('Four')
else:
    print('Three')