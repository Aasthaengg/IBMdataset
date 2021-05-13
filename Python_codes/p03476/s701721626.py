is_Prime = [True] * (10**5 + 1)
is_Prime[0] = False
is_Prime[1] = False
for i in range(2, int((10**5+1)**0.5)+1):
    for j in range(2*i, 10**5+1, i):
        is_Prime[j] = False
P = [i for i in range(10**5+1) if is_Prime[i] and is_Prime[(i+1)//2]]
odd = [0 for i in range(10**5+2)]
odd[0] = 0
for i in range(1, len(odd)):
    odd[i] = odd[i-1]
    if i in P:
        odd[i] += 1
Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    print(odd[r]-odd[l-1])