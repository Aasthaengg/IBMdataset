s = input()
d_memo = [chr(i) for i in range(97, 97+26)]
s_memo = set(list(s))

def next_c(sub_s, b_c):
    c = None
    for d in d_memo:
        if d not in set(list(sub_s)):
            if d > b_c:
                c = d
                break
    return c

if len(s) < len(d_memo):
    c = next_c(s, '')
    ans = s+c
else:
    b_c = ''
    ans = None
    for i in range(len(s)+1):
        c = next_c(s[:len(s)-i], b_c)
        if c is not None:
            ans = s[:len(s)-i]+c
            break
        else:
            b_c = s[len(s)-i-1]

if ans is None:
    print('-1')
else:
    print(ans)