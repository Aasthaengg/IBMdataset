box = list(input().split())
an = list("1974")
if all(a in box for a in an):
    print("YES")
else:
    print("NO")