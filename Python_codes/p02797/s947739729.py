n, k, s = map(int, input().split())

other = s+1
if other > int(1e9):
    other -= 2

print(*([s]*k + [other]*(n-k)))