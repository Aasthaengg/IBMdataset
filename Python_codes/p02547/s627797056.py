n=int(input())
B=[False]*n
for i in range(n):
    d1,d2=map(int,input().split())
    B[i]=d1==d2
for i in range(n-2):
    if B[i] and B[i+1] and B[i+2]:
        print('Yes')
        break
else:
    print('No')