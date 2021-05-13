s = input()
n = len(s)


for i in range(n):
    # i回の操作でそれぞれのアルファベットについて
    # 全て同じ文字にできるかどうか
    table = [[0]*(n-i) for _ in range(26)]

    for j in range(n):
        x = s[j]
        x = ord(x)-ord('a')
        L = max(0, j-i)
        if table[x][L]:
            L += 1
        R = min(j+1, L+i+1, n-i)
        for k in range(L, R):
            table[x][k] = 1

    if any(0 not in row for row in table):
        print(i)
        break
