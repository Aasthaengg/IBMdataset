K,T = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=True)
a = A[0]
if a<=(K+1)//2:
    ans = 0
elif K%2==1:
    ans = (a-(K+1)//2)*2
else:
    ans = (a-(K+1)//2)*2-1
print(ans)