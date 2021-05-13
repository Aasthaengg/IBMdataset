N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

temp = [T-i*0.006 for i in H]

ans = 0
mindt = 100000
for i in range(N):
    if abs(A-temp[i])<mindt:
        ans=i+1
        mindt=abs(A-temp[i])
        
print(ans)