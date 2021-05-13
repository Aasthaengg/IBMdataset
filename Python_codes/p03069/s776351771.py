n = int(input())
s = list(input())
rw = s.count(".")
rb = n - rw
ans = rw
lw = 0
lb = 0
for i in s:
    if i == ".":
        lw += 1
        rw -= 1
    else:
        lb += 1
        rb -= 1
    ans = min(ans, lb + rw)
print(ans)