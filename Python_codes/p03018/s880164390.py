s = input()
s_= s.replace("A", "0").replace("BC", "1").replace("B", "2").replace("C", "2")
s_012 = list(map(int, list(s_)))
count = 0
i = 0
ans = 0
while i < len(s_012):
    if s_012[i] == 0:
        count += 1
    elif s_012[i] == 1:
        ans += count
    else:
        count = 0
    i += 1

print(ans)