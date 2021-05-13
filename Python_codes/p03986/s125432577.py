S = input()

T_count = 0
S_count = 0
ans = 0
for i in range(len(S)):
    if S[i] == "S":
        S_count += 1
    else:
        if S_count > T_count:
            T_count += 1
        else:
            ans += 2
            
print(ans)