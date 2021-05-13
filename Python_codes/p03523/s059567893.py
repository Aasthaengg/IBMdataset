a = input()
s = 'AKIHABARA'

a_idx = 0
s_idx = 0
ans = 'YES'
while a_idx < len(a) and s_idx < len(s):
    if a[a_idx] != s[s_idx]:
        if s[s_idx] == 'A':
            s_idx += 1
            continue
        else:
            ans='NO'
            break
    a_idx += 1 
    s_idx += 1 

if s_idx == len(s) and a_idx != len(a) :
    ans = 'NO'

if s_idx != len(s) and a_idx == len(a) :
    if s[s_idx] == 'A' and len(s[s_idx:]) == 1:
        ans = 'YES'
    else:
        ans = 'NO'
print(ans)