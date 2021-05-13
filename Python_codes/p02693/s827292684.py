a=0
K=int(input())
A,B=map(int,input().split())
for i in range(1,1001):
    if A<=K*i<=B:
        a=1
        break
if a==0:
    print('NG')
else:
    print('OK')