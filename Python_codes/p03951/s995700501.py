def main():
    N = int(input())
    s = list(input())
    t = list(input())

    cnt = 0
    for i in range(N):
        stmp = s[N-i-1:]
        ttmp = t[:i+1]
        if stmp == ttmp:
            cnt = i+1
        
    ans = 2*N - cnt
    print(ans)

if __name__ == "__main__":
    main()
