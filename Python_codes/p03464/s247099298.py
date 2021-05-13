K = int(input())
As = list(map(int, input().split()))

# answer will be "{lo} {hi}"
lo = 2
hi = 2
for A in reversed(As):
    if (hi // A) - ((lo - 1) // A) == 0:
        print(-1)
        exit()
    lo = (lo + A - 1) // A * A
    hi = (hi // A + 1) * A - 1 

print(lo, hi)