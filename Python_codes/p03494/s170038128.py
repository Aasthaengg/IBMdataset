N = int(input())
A = [int(s) for s in input().split()]

def func_half(x):
    result = 0
    if x % 2 == 0:
        i = 1
        while x % (2**i) == 0:
            result = i
            i += 1
    return result

ans = 10**9
for a in A:
    buf = func_half(a)
    if buf == 0:
        ans = 0
        break
    ans = min(ans, buf)

print(ans)