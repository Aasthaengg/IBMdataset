k, x = list(map(int, input().split()))
ans = []
for i in range(x - k + 1, x + k):
    ans.append(str(i))
print(" ".join(ans))