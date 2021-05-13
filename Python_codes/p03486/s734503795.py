S = input()
T = input()
S_len = len(S)
T_len = len(T)
S_sorted = sorted(S)
T_sorted = sorted(T, reverse=True)
ans = True
for i in range(min(S_len, T_len)):
    s = ord(S_sorted[i])
    t = ord(T_sorted[i])
    if s < t:
        print('Yes')
        exit(0)
    if s == t:
        continue
    else:
        print('No')
        exit(0)
if S_len >= T_len:
    print('No')
else:
    print('Yes')
