_N = int(input())
N = _N

i = 1
div = set()
ans = 0
while i*i <= N:
    if N % i == 0:
        div.add(i)
        div.add(N//i)
    i += 1

for d in div:
    m = _N//d-1
    if m > d:
        ans += m
print(ans)
