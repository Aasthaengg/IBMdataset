S = input()

ans = "WA"

if S[0]=="A" and S[2:-1].count("C")==1:
    if S[1:].replace("C","c").islower():
        ans = "AC"

print(ans)