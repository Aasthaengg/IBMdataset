N = int(input())
S = [input() for _ in range(N)]
counter1 = 0
counter2 = 0
counter3 = 0
for s in S:
    if s[-1] == "A":
        if s[0] == "B":
            counter1 += 1
        else:
            counter2 += 1
    elif s[0] == "B":
        counter3 += 1
ans = 0
if counter1 == 0:
    ans += min(counter2, counter3)
else:
    if counter2 + counter3 > 0:
        ans += (counter1 + min(counter2, counter3))
    else:
        ans += (counter1 - 1)

for s in S:
    ans += s.count("AB")
print(ans)
