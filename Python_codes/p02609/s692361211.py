N = int(input())
X = input()

n1 = X.count("1")
Xn = int(X, 2)

Xms = (Xn % (n1 - 1)) if n1 > 1 else 0
Xml = Xn % (n1 + 1)

p2s = [1]
p2l = [1]
s2 = 1
l2 = 1
for i in range(N - 1):
    s2 = (s2 * 2) % (n1 - 1) if n1 > 1 else 0
    l2 = (l2 * 2) % (n1 + 1)
    p2s.append(s2)
    p2l.append(l2)


def f(n):
    if n == 0:
        return 0
    return f(n % bin(n).count("1")) + 1


for i in range(N):
    cnt = 0
    p2 = 2 ** (N - i - 1)
    Xim = 0

    if X[i] == "1" and n1 == 1:
        print(cnt)
        continue
    elif X[i] == "1":
        Xim = (
            Xms - p2s[-i - 1]
            if Xms - p2s[-i - 1] >= 0
            else ((n1 - 1) + (Xms - p2s[-i - 1]))
        )
    else:
        Xim = (
            Xml + p2l[-i - 1]
            if Xml + p2l[-i - 1] < (n1 + 1)
            else (Xml + p2l[-i - 1] - (n1 + 1))
        )
    print(f(Xim) + 1)

