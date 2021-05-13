def count_divisor(n):
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            arr.append(i)
            arr.append(n//i)
    res = len(set(arr))
    return res

n = int(input())
ans = 0
for i in range(1, n+1, 2):
    c = count_divisor(i)
    if c == 8: ans += 1
print(ans)