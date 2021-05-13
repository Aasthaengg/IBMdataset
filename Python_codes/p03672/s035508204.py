def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    s = input()
    n = (len(s)-1)//2
    ans = 0
    for i in range(1,n+1):
        if (s[:i] == s[i:2*i]):
            ans = 2*i
    print(ans)




if __name__ == '__main__':
    main()