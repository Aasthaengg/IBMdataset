n, k, q = map(int, input().split())
#a = [int(input()) for _ in range(q)]
ans = [k - q] * n

for i in range(q):
    ans[int(input()) - 1] += 1

for t in ans:
    if t > 0:
        print("Yes")
    else:
        print("No")
