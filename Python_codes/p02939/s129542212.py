S = input()

ans = 0
A = ""
B = ""
for s in S:
    A += s
    if A != B:
        ans += 1
        A, B = "", A
print(ans)
