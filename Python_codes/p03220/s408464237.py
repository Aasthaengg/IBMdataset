N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
ans = 10**6
te = 0
I = int()
for i in range(N):
    te = T-H[i]*0.006
    if abs(A-te) < ans:
        ans = abs(A-te)
        I = i
print(I+1)