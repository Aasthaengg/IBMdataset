def p(S):
    str = ""
    for s in S:
        str += chr(ord("a")+int(s))
    print(str)

N = int(input())
S = [0]*N

def up(i):
    if i == 0:
        return True
    S[i] += 1
    if S[i] == max(S[:i]) + 2:
        S[i] = 0
        return up(i-1)
    return False

while True:
    p(S)
    if up(N-1):
        break
