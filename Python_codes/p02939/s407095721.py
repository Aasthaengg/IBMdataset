s = input()
n = len(s)
s += s[-1]
ans = 0
pos = 0
is_len_1 = False
is_now = ""
while pos < n:
    if is_len_1:
        if s[pos - 1] == s[pos]:
            pos += 2
            is_len_1 = False
            is_now = s[pos : pos + 2]
        else:
            pos += 1
            is_now = s[pos : pos + 1]
    else:
        pos += 1
        is_len_1 = True
        is_now = s[pos : pos + 1]
    ans += 1
if pos == n + 1:
    ans -= 1
print(ans)
