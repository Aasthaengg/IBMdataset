w = input().lower()
ans = 0
while 1:
    s = input()
    if s == "END_OF_TEXT":
        break
    s = s.lower().split()
    ans += s.count(w)
print(ans)

