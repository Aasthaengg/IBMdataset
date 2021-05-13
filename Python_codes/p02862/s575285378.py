def main():
    import sys
    readline = sys.stdin.buffer.readline

    x, y = map(int, readline().split())

    if (x+y) % 3 != 0 or y > 2*x or y < x/2:
        print(0)
        exit()
    
    mod = 10**9 + 7
    xy = (x + y) // 3
    z = min(x-xy, y-xy)
    ans = 1
    for i in range(1, z+1):
        ans = (ans * (xy-i+1)) % mod
        ans = (ans * pow(i, mod-2, mod)) % mod
    print(ans)

if __name__ == '__main__':
    main()