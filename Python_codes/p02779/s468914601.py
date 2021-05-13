n=int(input())
l=list(map(int,input().split()))
k=set(l)
if n==len(k):
    print('YES')
else:
    print('NO')