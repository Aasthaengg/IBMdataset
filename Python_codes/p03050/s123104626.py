def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    i = 1
    ans = 0
    while i*i < n:
        if n%i == 0:
            tmp = n//i -1
            if i < tmp:
                ans += n//i - 1
        i+= 1
    print(ans)




    
if __name__ == '__main__':
    main()