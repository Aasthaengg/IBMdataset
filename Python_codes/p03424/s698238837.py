N=int(input())
S=list(input().split())
a=len(list(set(S)))
if a==3:
    print('Three')
elif a==4:
    print('Four')