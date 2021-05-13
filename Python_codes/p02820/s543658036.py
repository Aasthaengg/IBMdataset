n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
 
did = "-" * k
ans = 0
for i in t:
    if i == "r":
        if did[-k] == "p":
            did += "-"
        else:
            did += "p"
            ans += p
    elif i == "s":
        if did[-k] == "r":
            did += "-"
        else:
            did += "r"
            ans += r
    else:
        if did[-k] == "s":
            did += "-"
        else:
            did += "s"
            ans += s
 
print(ans)