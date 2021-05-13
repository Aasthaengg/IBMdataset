S = raw_input()
P = raw_input()
no_flg = True
count = S.count(P[0])
start = 0
for c in range(count):
    i = 1
    if c > 0:
        start = S[(start+1):].index(P[0]) + (start+1)
    else:
        start = S[start:].index(P[0])
    for p in P[1:]:
        if S[(start+i) % len(S)] != p:
            break
        i += 1
    if i == len(P):
        print 'Yes'
        no_flg = False
        break
if no_flg:
    print 'No'