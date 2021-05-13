n = int(input())
up = list(map(int, input().split()))
low = list(map(int, input().split()))

left = [up[0]]
right = [0 for i in range(n)]
right[-1] = low[-1]
for i in range(1, n):
    left.append(left[i-1] + up[i])
for i in range(n-2, -1, -1):
    right[i] = right[i+1] + low[i]

ans = 0
for i in range(n):
    ans = max(left[i] + right[i], ans)
print (ans)