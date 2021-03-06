def main():
    n = int(input())
    R, B = [], []
    for i in range(n):
        R.append(list(map(int, input().split())) + [0, i])
    for _ in range(n):
        B.append(list(map(int, input().split())))
    B.sort(key = lambda x: x[0])
    ans = 0
    for b in B:
        f = list(filter(lambda x: x[0] < b[0] and x[1] < b[1] and x[2] == 0, R))
        if len(f) != 0:
            f.sort(key = lambda x: x[1], reverse = True)
            p = f[0]
            ans += 1
            R[p[3]][2] = 1
    print(ans)        

if __name__ == '__main__':
    main()
