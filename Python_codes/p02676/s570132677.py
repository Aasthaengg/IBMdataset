K = int(input())
S = list(input())

s = "".join(S[:K])
c = len(S)

if K >= c:
    print(s)
else:
    answer = s + "..."
    print(answer)
