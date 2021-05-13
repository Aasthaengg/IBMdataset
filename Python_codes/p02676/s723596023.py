k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    S = s[:k]
    print(S, end="")
    print("...")