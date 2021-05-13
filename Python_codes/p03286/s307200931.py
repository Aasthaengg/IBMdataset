N = int(input())
ans = ''
for _ in range(1000):
    r = N % 2
    if r < 0:
        r += 2
    N = (N-r)//(-2)
    ans = str(r) + ans
print(int(ans))