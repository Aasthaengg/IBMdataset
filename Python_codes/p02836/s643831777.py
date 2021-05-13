def main():
    S = input()
    n = len(S)
    ans = 0
    for i in range(n//2):
        if not S[i]==S[n-i-1]:
            ans += 1
    print(ans)

main()
