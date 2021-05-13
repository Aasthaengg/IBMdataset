from itertools import product
S = input()
n = len(S)
bit = list(product([0, 1], repeat = n - 1))
ans = 0
for state in bit:
    s = S[0]
    for i in range(len(state)):
        if state[i] == 1:
            s += '+' + S[i + 1]
        else:
            s += S[i + 1]
    ans_list = list(map(int,s.split('+')))
    for a in ans_list:
        ans += a
print(ans)
