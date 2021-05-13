n = int(input())
A = list(map(int, input().split()))

rate = [0]*8
f = 0

for a in A:
    if a >= 3200:
        f += 1
    else:
        rate[a//400] = 1

if sum(rate) > 0:
    print(f"{sum(rate)} {sum(rate)+f}")
else:
    print(f"{min(f, 1)} {f}")