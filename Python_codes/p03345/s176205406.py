A,B,C,K=map(int,input().split())

t=A-B
if 10**18<t:
    print('Unfair')
elif K%2==0:
    print(t)
else:
    print(-t)