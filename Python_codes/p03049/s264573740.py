N = int(input())
ans = 0
Count_A = 0
Count_B = 0
Count_BA = 0
s = []
for _ in range(N):
    s.append(input())

for i in range(N):
    ans += s[i].count("AB")
    if s[i][0] == "B" and s[i][-1] == "A":
        Count_BA += 1
    elif s[i][0] == "B":
        Count_B += 1
    elif s[i][-1] == "A":
        Count_A += 1

if Count_BA == 0:
    ans += min(Count_A, Count_B)
elif Count_A + Count_B == 0:
    ans += Count_BA-1
else:
    ans += Count_BA + min(Count_A, Count_B)

print(ans)