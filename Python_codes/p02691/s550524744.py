N = int(input())
A = [int(n) for n in input().split()]

D = dict()
ans = 0
for i, a in enumerate(A):
    val = i - a
    if val in D.keys():
        ans += D[val]
        
    val = i + a
    if val not in D.keys():
        D[val] = 0
    D[val] += 1
    
print(ans)
