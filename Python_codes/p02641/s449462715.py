x,n = map(int, input().split())
P = list(map(int, input().split()))

for i in range(1000):
    right = x-i
    left = x+i

    if right not in P:
        ans = right
        break

    if left not in P:
        ans = left
        break
print(ans)