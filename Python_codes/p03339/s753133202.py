N = int(input())
S = input()

l = 0
r = S.count("E", 1, len(S))
ans = l + r
for i in range(1, len(S)):
    if S[i] == "E":
        r -= 1
    if S[i - 1] == "W":
        l += 1

    ans = ans if ans <= l + r else l + r

print(ans)