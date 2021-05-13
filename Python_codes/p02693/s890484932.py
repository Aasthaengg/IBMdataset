def main():
    n = int(input())
    s = list(map(int,input().strip().split()))

    if s[0] % n == 0 or s[1] % n == 0:
        print("OK")
        return 

    for nn in range(s[0], s[1]):
        if nn % n == 0:
            print("OK")
            return 
    print("NG")
    return

main()
