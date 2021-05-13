import string
N = int(input())
L = string.ascii_lowercase
ans = []

while N > 0:
    s = N % 26
    N  = (N - 1) // 26
    ans.append(L[s-1])

ans.reverse()
print("".join(ans))