def main():
    N = int(input())
    S = list(input())
    cnt = 0; ans = 0
    for s in S:
        cnt += (s == 'I') - (s == 'D')
        ans = max(cnt, ans)
    print(ans)

if __name__ == "__main__":
    main()
