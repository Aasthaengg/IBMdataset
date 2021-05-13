N = int(input())
S = str(N)

if S[0] == S[1] == S[2]:
    print(N)
else:
    print(111 * (N // 111 + 1))