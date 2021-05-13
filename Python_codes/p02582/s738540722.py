S = list(input())
ans = S.count("R")
if S[1] != "R" and ans == 2:
    ans -= 1
print(ans)
