N = int(input())
Ss = [[1], [1]]
while True:
    k = len(Ss)
    m = k * (k - 1) // 2
    if N < m:
        print("No")
        break
    elif N == m:
        print("Yes")
        print(k)
        for S in Ss:
            print(len(S), " ".join(map(str, S)))
        break
    S_new = []
    for i in range(k):
        x = m + 1 + i
        Ss[i].append(x)
        S_new.append(x)
    Ss.append(S_new)