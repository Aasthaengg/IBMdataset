def solve():
    S = input()
    tmp = ''
    ans = 0
    i = 0
    while i < len(S):
        s = S[i]
        if s != tmp:
            ans += 1
            i += 1
            tmp = s
        else:
            ans += 1 if i != len(S) - 1 else 0
            i += 2
            tmp = ''
    print(ans)
    
if __name__ == "__main__":
    solve()