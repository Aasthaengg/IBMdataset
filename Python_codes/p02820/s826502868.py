n, k = map(int, input().split())
r, s, p = map(int, input().split())
T = list(input())
P = {'s':r, 'p':s, 'r':p}
 
mx = r*T.count('s')+s*T.count('p')+p*T.count('r')
if len(T)<k:
    print(mx)
else:
    for i in range(n-k):
        if T[i]==T[i+k]:
            mx -= P[T[i]]
            T[i+k] = '_'
print(mx)
