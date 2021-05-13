from collections import Counter

N = int(input())
A = list(map(int, input().split()))

if A.count(0) == N:
    print("Yes")
    exit()

d = Counter(A)
if len(d.keys()) > 3:
    print("No")
    exit()
elif len(d.keys()) == 3:
    a, b, c = d.keys()
    if d[a] == d[b] == d[c] and a ^ b ^ c == 0:
        print("Yes")
    else:
        print("No")
    exit()
elif len(d.keys()) == 2:
    a, b = d.keys()
    if a * b != 0:
        print("No")
    else:
        if a != 0:
            d[a], d[b] = d[b], d[a]  # aを0にする
        if d[a] * 3 == N and 3 * d[b] == 2 * N:
            print("Yes")
        else:
            print("No")
    exit()
print("No")

