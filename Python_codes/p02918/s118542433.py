import re
N, K = map(int, input().split())
S = input()
S = re.sub(r"R+", "R", S)
S = re.sub(r"L+", "L", S)
L_num = S.count("L")
num = min(L_num, N - L_num)

if num <= K:
    print(N - 1)
else:
    print(N - len(S) + 2 * K)