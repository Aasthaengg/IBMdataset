import collections
import itertools

N = int(input())
S = [input()[0] for _ in range(N)]
A = []
ans = 0

for i in S:
    if i == 'M' or i == 'A' or i == 'R' or i == 'C' or i == 'H':
        A.append(i)
        
if len(A) != 0:       
    C = collections.Counter(A).most_common()
    v,c = zip(*C)
    #print(C)
    #print(c)

    for a,b,c in itertools.combinations(c,3):
        #print(a,b,c)
        ans += a*b*c

print(ans)



