A,B,C,D,E,F = map(int,input().split())

ws = set()
for a in range(F+1):
    if a*100*A > F: break
    for b in range(F+1):
        if a*100*A + b*100*B > F: break
        ws.add(a*100*A + b*100*B)

ss = set()
for c in range(F+1):
    if c*C > F: break
    for d in range(F+1):
        if c*C + d*D > F: break
        ss.add(c*C + d*D)

os = -1
ow = 999
for w in ws:
    if w==0: continue
    for s in ss:
        if s+w > F: continue
        if w*E < s*100: continue
        if os * (s+w) < s * (os+ow):
            os,ow = s,w
print(os+ow, os)