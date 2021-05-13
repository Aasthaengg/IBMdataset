N, M = map(int, input().split())
A = list(map(int, input().split()))
CB = []

for _ in range(M):
    b, c = map(int, input().split())
    CB.append((c, b))

CB.sort(reverse=True)
A.sort()
ans = 0
now = 0
count = 0
for i in range(len(A)):
    if A[i] >= CB[now][0]:
        ans += A[i]
    else:
        ans += CB[now][0]
        count += 1
    
    if count == CB[now][1]: # 枚数を超えたら
        count = 0
        now += 1
    if now >= len(CB):
        stoped_idx = i
        ans += sum(A[stoped_idx + 1:])
        break
print(ans)