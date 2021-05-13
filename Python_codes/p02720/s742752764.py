K = int(input())

l = []

def c(depth, a, d):
    ans = 0
    if depth == d:
        l.append(a)
        return
    if int(a[-1]) - 1 >= 0:
        c(depth + 1, a + str(int(a[-1]) - 1), d)
    c(depth + 1, a + a[-1], d)
    if int(a[-1]) + 1 <= 9:
        c(depth + 1, a + str(int(a[-1]) + 1), d)
    return

for d in range(10):
    for i in range(1, 10):
        c(0, str(i), d)
        
print(l[K - 1])