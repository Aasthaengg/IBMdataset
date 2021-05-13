n = int(input())
p_index = [0] * n
for i in range(n):
    p_index[int(input())-1] = i
prev = 10**9
ans = 0
val = 1
for item in p_index:
    if prev > item:
        val = 1
    else:
        val += 1
    prev = item
    ans = max(ans, val)
print(n-ans)