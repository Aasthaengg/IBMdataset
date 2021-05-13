n,m = map(int, input().split())
a = list(map(int, input().split()))

votes = sum(a)
a.sort(reverse=True)

print("Yes") if all(e >= votes/(4*m) for e in a[:m]) else print("No")