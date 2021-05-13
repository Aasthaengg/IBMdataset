from collections import defaultdict

Dic = defaultdict(int)
H, W, N = map(int, input().split())
ans = [0]*10

for i in range(N):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 1 <= a + dy <= H-2 and 1 <= b + dx <= W-2:
                Dic[(a+dy, b+dx)] += 1

for i in Dic:
    ans[Dic[i]] += 1
ans[0] = (H-2)*(W-2) - sum(ans)

for i in ans:
    print(i)
