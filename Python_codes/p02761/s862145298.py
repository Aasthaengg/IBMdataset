n, m = map(int, input().split())
j = [True]*(n + 1)
l = [1] + [0]*(n - 1)
jud = True
for i in range(m):
    s, c = map(int, input().split())
    if s == 1 and c == 0 and n != 1:
        jud = False
    if j[s]:
        l[s - 1] = c
        j[s] = False
    else:
        if l[s - 1] != c:
            jud = False
if not jud:
    print(-1)
elif n == 1 and m == 0:
    print(0)
else:
    print("".join(list(map(str, l))))
