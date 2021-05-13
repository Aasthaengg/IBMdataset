S = input()

X = [S.count(ch) for ch in "abc"]

T = ("ABC" * (len(S) // 3 + 1))[:len(S)]
Y = [T.count(ch) for ch in "ABC"]

if set(X) == set(Y):
    print("YES")
else:
    print("NO")

