K = int(input())
now = 7
for i in range(K):
    if now % K == 0:
        print(i + 1)
        exit(0)
    now = (10 * now + 7) % K
print("-1")
