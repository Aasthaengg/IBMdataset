
S = input()
N = len(S)

increasing = S[0] == '<'
A = [] if increasing else [1]
cnt = 0
for c in S:
    f = c == '<'
    if f == increasing:
        cnt += 1
    else:
        A.append(cnt*(increasing*2-1))
        increasing = not increasing
        cnt = 1
A.append(cnt*(increasing*2-1))

if A[-1] > 0:
    A.append(-1)

m = iter(A)
res = 0

for a,b in zip(m,m):
    b = -b
    if a > b:
        a,b = b,a
    res += ((a-1)*a+(b+1)*b)

print(res//2)