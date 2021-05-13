def search(S,t):
    for s in S:
        if t == s:
            return True
    return False

n = int(raw_input())
S = map(int,raw_input().split(' '))
q = int(raw_input())
T = map(int,raw_input().split(' '))


ret = 0
for t in T:
    if search(S,t):
        ret += 1
print ret