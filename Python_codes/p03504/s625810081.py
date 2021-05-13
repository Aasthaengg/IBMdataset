def main():
    N,C = [int(_n) for _n in input().split()]
    L = 100010
    table = [[0]*L for _ in range(C)]
    for i in range(N):
        s,t,c = [int(_n) for _n in input().split()]
        c -= 1
        s -= 1
        t -= 1
        table[c][s] += 1
        table[c][t+1] -= 1 
    for c in range(C):
        for j in range(L-1):
            table[c][j+1] += table[c][j]
    for i in range(C):
        for j in range(L):
            table[i][j] = min(1, table[i][j])
    for j in range(L):
        for c in range(C-1):
            table[c+1][j] += table[c][j]
    print(max(table[C-1]))
    # print(table)
    # print(table)
    # acc = [0] * len(times)
    # progs.sort(key = lambda x:x[2])



main()