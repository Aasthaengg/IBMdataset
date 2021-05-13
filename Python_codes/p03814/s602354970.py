S = list(input())

count1 = 0
count2 = 0

for i in range(200000):
    if S[i] == "A":
        count1 = i
        break

for i in range(1, 200000 + 1):
    if S[-i] == "Z":
        count2 = i
        break

ans = len(S) - (count1 + count2) + 1
print(ans)