n, k, q = list(map(int, input().split()))

collect = [0] * (n+1)
for i in range(q):
    p = int(input())
    collect[p] += 1

for j in range(1, n+1):
    if k - (q - collect[j]) > 0:
        print("Yes")
    else:
        print("No") 