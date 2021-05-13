import copy

s = list(input())
n = len(s) - 1

ans = 0
for bit in range(1 << n):

    #print(bin(bit))

    p = []
    for i in range(n):
        if bit & (1 << i):
            p.append(i)
    #print(p)

    m = 1
    s_ = copy.copy(s)
    for idx in p:
        s_[idx+m:idx+m] = '+'
        m += 1
    #print(s_)

    ss = ''.join(s_)
    #print(ss)
    ans += sum([int(n) for n in ss.split('+')])

print(ans)