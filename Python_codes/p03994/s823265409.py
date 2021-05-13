alpha = "abcdefghijklmnopqrstuvwxyz"
A = ["a"]+[i for i in alpha[::-1]]
s = list(input())
k = int(input())
n = len(s)
for i in range(n):
    if s[i] == "a":
        continue
    j = A.index(s[i])
    if j <= k:
        s[i] = "a"
        k -= j
    if k == 0:
        print("".join(s))
        exit()
else:
    k %= 26
    l = alpha.index(s[-1])
    if l + k <= 25:
        s[-1] = alpha[k+l]
    else:
        s[-1] = alpha[k+l-26]
    print("".join(s))