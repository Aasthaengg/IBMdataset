n = int(input())
h = list(map(int, input().split()))
ans, val0, val1 = 0, 0, 0

for j, i in enumerate(h):
    if val0 > i:
        ans += val0-val1
        val1 = i
    elif j == len(h)-1:
        val0 = i
        ans += val0-val1
    val0 = i
print(ans)
