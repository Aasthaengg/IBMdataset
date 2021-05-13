n = int(input())
s = input()
w = s.count(".")
b = n-w
ans = min(w,b)
b = 0
for i in range(n):
    if s[i] == ".":
        w -= 1
    else:
        b += 1
    ans = min(ans,w+b)
print(ans)

