n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
prev = -1
for i in A:
    ans += B[i-1]
    if prev == i-1:
        ans += C[i-2]
    prev=i
print(ans)