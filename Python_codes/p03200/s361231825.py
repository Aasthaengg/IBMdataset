S = input()
W = S.count("W")
ans = 0
for i in range(len(S)):
    if S[i] == "W":
        ans += i
ans -= W*(W-1)//2
print(ans)