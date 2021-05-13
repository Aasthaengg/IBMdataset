s = input()
t = input()
result = []
st = len(s) - len(t)
for i in range(st+1):
    _ = s[:i]
    flg = False
    for j in range(i, i+len(t)):
        if s[j] == t[j-i]:
            _ += t[j-i]
        elif s[j] == '?':
            _ += t[j-i]
        else:
            flg = True
    
    if flg == False:
        _ += s[i+len(t):]
        _ = _.replace('?', 'a')
        result.append(_)

if len(result) != 0:
    result.sort()
    print(result[0])
else:
    print('UNRESTORABLE')