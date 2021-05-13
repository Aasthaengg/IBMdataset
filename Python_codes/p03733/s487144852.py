def solve():
    N,T = map(int,input().split())
    t = list(map(int, input().split()))
    dup = 0
    for i in range(N-1): #enumerateはendが選択できない
        if t[i+1] < t[i] + T:
            dup += T-(t[i+1] - t[i])

    print(N*T - dup)




if __name__ == '__main__':
    solve()
