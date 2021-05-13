S = input()

ans = "WA"

if S[0] == "A":
    if S[2:-1].count("C") == 1:
        removed_str = S[1] + S[2:-1].replace("C", "") + S[-1]
        if removed_str.islower():
            ans = "AC"

print(ans)
