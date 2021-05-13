n, k, c = map(int, input().split())
s = input()
L = [0]
R = [0]
i = 1
while i <= n:
    if s[i-1] == 'o':
        L.append(i)
        i += c+1
    else:
        i += 1
i = n
while i >= 1:
    if s[i-1] == 'o':
        R.append(i)
        i -= c+1
    else:
        i -= 1
# print(L)
# print(R)
for i in range(1, min(len(L), len(R))):
    if L[i] == R[k-i+1]:
        print(L[i])