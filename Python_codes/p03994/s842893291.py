import sys
sys.setrecursionlimit(10**7)

alphabets = "abcdefghijklmnopqrstuvwxyz"
a = {c:i for i, c in enumerate(alphabets)}
s = list(input())
n = len(s)
k = int(input())

def f(k, i):
    if i == n - 1:
        k_ = k % 26
        c = s[i]
        shifted = (k_ + a[c]) % 26
        return alphabets[shifted]

    c = s[i]
    diff = 26 - a[c]
    if c != "a" and diff <= k:
        return "a" + f(k-diff, i+1)
    else:
        return c + f(k, i+1)
        

print(f(k, 0))