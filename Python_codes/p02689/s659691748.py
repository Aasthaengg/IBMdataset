N, M = map(int, input().split())
H = list(map(int, input().split()))
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    #0_index
    A[i] -= 1
    B[i] -= 1

ans = [1] * N

for i in range(M):
    a_height = H[A[i]]
    b_height = H[B[i]]
    if a_height < b_height:
        ans[A[i]] = 0
    elif a_height == b_height:
        ans[A[i]] = 0
        ans[B[i]] = 0
    else:
        ans[B[i]] = 0

#print("ans", ans)
print(ans.count(1))
