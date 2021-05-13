n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

for i in range(k):
    # print(t[i::k])
    t0 = t[i]
    cnt = 1
    for t1 in t[i+k::k]:
        if t0 == t1:
            t = t[:i+cnt*k] + 'n' + t[i+cnt*k+1:]
            t0 = 'n'
        else:
            t0 = t1
        cnt += 1

print(p*t.count('r')+r*t.count('s')+s*t.count('p'))
