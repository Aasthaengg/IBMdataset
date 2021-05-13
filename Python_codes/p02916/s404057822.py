N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
prev = -2
for x in A:
    ans += B[x-1]
    if x==prev+1:
        ans += C[x-2]
    prev = x
print(ans)