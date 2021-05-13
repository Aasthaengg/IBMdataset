#codinf utf-8
s = list(input())
K = int(input())
N = len(s)
alp = [chr(i) for i in range(97, 97+26)]

for i in range(N):
    idx = alp.index(s[i])
    
    if K + idx >= 26 and idx != 0:
        K = K - ( 26 - idx )
        s[i] = 'a'
    if K == 0:
        break
    
if K > 0:
    id = alp.index(s[N-1])

    id_ = ( id + K ) % 26

    s[N-1] = alp[id_]

print(''.join(s))