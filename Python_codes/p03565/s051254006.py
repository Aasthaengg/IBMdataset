s = input()
t = input()
sn = len(s)
tn = len(t)

if sn < tn:
    print("UNRESTORABLE")
    quit()
    
for i in range(sn-tn, -1, -1):
    matched = True
    for j in range(tn):
        if s[i+j] != t[j] and s[i+j] != '?':
            matched = False
            break
    if matched:
        break
        
if not matched:
    print("UNRESTORABLE")
    quit()

ans = ['a'] * sn
for j in range(0, i):
    if s[j] != '?':
        ans[j] = s[j]
for j in range(tn):
    ans[i + j] = t[j]
for j in range(i + tn, sn):
    if s[j] != '?':
        ans[j] = s[j]

print("".join(ans))