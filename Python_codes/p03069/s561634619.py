def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    s = input()
    cnt = [0]
    for i in range(n):
        cnt.append(cnt[-1])
        if s[i] == '#':
            cnt[-1] += 1
    
    m = cnt[-1]
    ans = 10**9
    for i in range(n+1):
        tmp = cnt[i] + (n-i)-(m-cnt[i])
        ans = min(tmp, ans)
    print(ans)


        
        
if __name__ == '__main__':
    main()