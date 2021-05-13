S = list(str(input()))

count = 0
Wcount = 0


for i in range(len(S)):
    if S[i] == "W":
        count += i - Wcount
        Wcount += 1

print(count)
