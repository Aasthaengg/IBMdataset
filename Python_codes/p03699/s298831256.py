n = int(input())
a = [int(input()) for x in range(n)]
total = sum(a)
if not total % 10:
    a.sort()
    for v in a:
        if v % 10:
            total -= v
            break

print(total if total % 10 else 0)