a, b, c = [int(w) for w in input().split()]

cond = False
for n in range(a, a*b+1, a):
    if n % b == c:
        cond = True
        break

print("YES" if cond else "NO")
