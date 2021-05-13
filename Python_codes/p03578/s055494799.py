from collections import Counter
n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))
Dc = Counter(D)
Tc = Counter(T)
for t in Tc.keys():
    if Dc.get(t) == None:
        print('NO')
        exit()
    if Tc[t] > Dc[t]:
        print('NO')
        exit()
print('YES')