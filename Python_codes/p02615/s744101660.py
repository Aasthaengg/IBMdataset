#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse = True)
    ans = a[0]
    n -= 2
    i = 1
    while n > 0:
        if n == 1:
            ans += a[i]
            break
        else:
            ans += 2 * a[i]
            i += 1
            n -= 2
    print(ans)
    return

if __name__ == "__main__":
    main()