def main():
    sx,sy,tx,ty = map(int,input().split())
    tx = tx-sx
    ty = ty-sy
    ans = ['R' for i in range(tx)]
    ans += ['U' for i in range(ty)]
    ans += ['L' for i in range(tx)]
    ans += ['D' for i in range(ty)]
    ans += ['D']
    ans += ['R' for i in range(tx+1)]
    ans += ['U' for i in range(ty+1)]
    ans += ['L', 'U']
    ans += ['L' for i in range(tx+1)]
    ans += ['D' for i in range(ty+1)]
    ans += ['R']
    print(''.join(ans))

if __name__ == "__main__":
    main()
