S = list(input())
T = list(input())

S.sort()
T.sort(reverse=True)

s = ''.join(map(str,S))
t = ''.join(map(str,T))

if t > s:
    print('Yes')
else:
    print('No')