s = input()
cnt = sorted([s.count("a"), s.count("b"), s.count("c")])
ans = "YES"
if cnt[1]-cnt[0] >= 2 or cnt[2]-cnt[0] >= 2 or cnt[2]-cnt[1] >= 2:
    ans = "NO"
print(ans)