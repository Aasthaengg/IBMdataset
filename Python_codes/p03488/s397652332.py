S = input()
X, Y = map(int, input().split())

def run_length(s) -> list:
    res = [[s[0], 1]]
    for i in range(1, len(s)):
        if res[-1][0] == s[i]:
            res[-1][1] += 1
        else:
            res.append([s[i], 1])
    return res

RL = run_length(S)
if RL[0][0] == 'T':
    RL = [['F', 0]] + RL

SIZE = len(S)
nx = 1 << SIZE
ny = 1 << SIZE

x_flag = 1
for i in range(0, len(RL), 2):
    s, l = RL[i]
    if i == 0:
        nx = nx << l
    else:
        x_flag = (x_flag + RL[i - 1][1]) % 2
        if x_flag:
            nx = (nx << l) | (nx >> l)
        else:
            ny = (ny << l) | (ny >> l)

if ((nx >> (SIZE + X)) & 1) & ((ny >> (SIZE + Y)) & 1):
    print("Yes")
else:
    print("No")