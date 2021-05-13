s,K = open(0).read().split()
K = int(K)
dista = [(123 - ord(x)) % 26 for x in s]
sa = sum(dista)
if K >= sa:
    print('a'*(len(s)-1)+chr(97+(K-sa)%26))
else:
    ans = []
    count = K
    for i in range(len(s)):
        if count >= dista[i]:
            ans.append('a')
            count -= dista[i]
        else:
            ans.append(s[i])
    if ans[-1] == 'a':
        ans[-1] = chr(97+(count%26))
    else:
        ans[-1] = chr(ord(ans[-1])+count)
    print(''.join(ans))