n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

#print()
T = 0
A = 0
for i in range(n):
    t, a = p[i]
    if t >= T and a >= A:
        T, A = t, a
    else:
        d1 = T // t
        d2 = A // a
        if T % t != 0: d1 += 1
        if A % a != 0: d2 += 1
        d = max(d1, d2)
        T, A = d * t, d * a
    #print(T, A)

print(T+A)  