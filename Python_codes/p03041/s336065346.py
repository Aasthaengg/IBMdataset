n, k = map(int,input().split())
s = list(input())
if s[k-1] == "A":
    s[k-1] = "a"
    print("".join(s))
elif s[k-1] == "B":
    s[k-1] = "b"
    print("".join(s))
else:
    s[k-1] = "c"
    print("".join(s))