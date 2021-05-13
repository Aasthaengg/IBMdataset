def main():
    n = int(input())
    S = input()
    l, r = 0, S.count('.')
    ans = l + r
    for i in range(n):
        if S[i] == '#': l += 1
        else: r -= 1
        ans = min(ans, l + r)
    print(ans)
    
if __name__ == '__main__':
    main()
