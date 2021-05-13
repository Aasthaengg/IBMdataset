N = int(input())
A = list(map(int,input().split()))
B = [0] * N # 踏み台の高さ
ans = 0
h = 0
for i in range(1,N):
    if A[i] < A[i-1]+B[i-1]:
        h = B[i-1]+A[i-1] - A[i]
    else:
        h = 0
    B[i] = h

for i in range(N):
    ans += B[i]

# print(B)
print(ans)
# 一個前しか見てない