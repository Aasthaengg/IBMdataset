from collections import Counter
 
N = int(input())
l = list(map(int, input().split()))
 
o = Counter(l[::2]).most_common()
e = Counter(l[1::2]).most_common()
 
if o[0][0] == e[0][0]:
    if len(o) == 1:
        print(N//2)
    else:
        e1, e2 = o[0][1], o[1][1]
        o1, o2 = e[0][1], e[1][1]
 
        res = min(N-e1-o2, N-e2-o1)
        print(res)
else:
    print(N - o[0][1] - e[0][1])