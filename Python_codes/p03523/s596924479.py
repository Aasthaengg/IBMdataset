s = input()
ans = "AKIHABARA"
if s.count("K")*s.count("I")*s.count("H")*s.count("B")*s.count("R") != 1:
    print("NO")
    exit()
now = 0
for i in s:
    while now < len(ans) and ans[now] != i:
        now += 1
    now += 1
if 8 <= now <= 9:
    print("YES")
else:
    print("NO")
