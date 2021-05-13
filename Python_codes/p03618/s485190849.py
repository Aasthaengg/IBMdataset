A = input()
N = len(A)
L = [0] * 26
for a in A:
    L[ord(a)-97] += 1
ans = N*(N-1)//2 + 1
for l in L:
    if l >= 2:
        ans -= l*(l-1)//2
print(ans)
