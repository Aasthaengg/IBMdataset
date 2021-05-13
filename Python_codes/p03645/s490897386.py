n, m = map(int, input().split())
f = [0]*200020
s = [0]*200020


for i in range(m):
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        f[max(a, b)] = 1
        if s[max(a, b)] == 1:
            print("POSSIBLE")
            exit()
    if a == n or b == n:
        s[min(a, b)] = 1
        if f[min(a, b)] == 1:
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")