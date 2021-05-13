def main():
    N = int(input())
    p = list(map(int, input().split()))
    c = {}
    f = []
    for i in range(N):
        if p[i] != i+1:
            c[p[i]] = i+1
            f.append(p[i])
    if len(c) > 2:
        print('NO')
    elif len(f) == 0 or (c[f[0]] == f[1] and c[f[1]] == f[0]):
        print('YES')
    else:
        print('NO')

main()  