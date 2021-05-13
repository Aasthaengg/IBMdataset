def main(S):
    N = len(S)
    if S == S[::-1] and S[:(N - 1) // 2] == S[:(N - 1) // 2][::-1] and S[(N + 1) // 2:] == S[(N + 1) // 2:][::-1]:
        return True
    else:
        return False
S = list(input())
if main(S) == True:
    print('Yes')
else:
    print('No')