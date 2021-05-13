S = input()


def solve(S):
    ans = 0
    for i in range(4):
        if S[i]=='+':
            ans += 1
        else:
            ans -= 1
    return ans
print(solve(S))