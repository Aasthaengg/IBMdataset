N, H = map(int, input().split())

A = []
B = []
Amax = 0
for _ in range(N):
    a, b = map(int, input().split())
    Amax = max(a, Amax)
    B.append(b)

B.sort(reverse=True)

res = 0
for b in B:
    if b > Amax:
        res += 1
        if H <= b:
            print(res)
            exit()
        H -= b
    else:
        break

print(res + (H // Amax + int(H % Amax != 0)))