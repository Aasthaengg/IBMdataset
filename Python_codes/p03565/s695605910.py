s = str(input())
t = str(input())
ns = len(s)
nt = len(t)
start = -1
for j in range(ns):
    if t[0] == s[j] or s[j] == '?':
        j_temp = j
        i_temp = 0
        is_ok = True
        while i_temp < nt - 1:
            i_temp += 1
            j_temp += 1
            if j_temp >= ns:
                is_ok = False
                break
            if s[j_temp] == '?' or s[j_temp] == t[i_temp]:
                if i_temp == nt - 1:
                    break
                continue
            if s[j_temp] != t[i_temp]:
                is_ok = False
                break
        if is_ok:
            start = max(j, start)
ans = ""
if start == -1:
    print("UNRESTORABLE")
    exit()
for i in range(ns):
    if start <= i < start + nt:
        ans += t[i - start]
    elif s[i] == "?":
        ans += "a"
    else:
        ans += s[i]
print(ans)