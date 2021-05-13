s = input()
n = len(s)
import string
DD = [chr(i) for i in range(ord("a"), ord("z")+1)]
D = {}
for i in range(len(DD)):
    D[DD[i]] = i
A = [0] * 26
ans = 1
for i in range(n):
    ans += i - A[D[s[i]]]
    A[D[s[i]]] += 1
print(ans)