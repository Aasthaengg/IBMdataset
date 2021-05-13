import collections
S = input()
A = collections.Counter(S)
a = A["a"]
b = A["b"]
c = A["c"]
if max(abs(a-b),abs(b-c),abs(c-a)) > 1:
    print("NO")
else:
    print("YES")