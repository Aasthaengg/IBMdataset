S = input()

B = 0
W = 0
ans = 0
for i in range(len(S)):
    if S[i] == "B":
        B += 1
    else:
        ans += i - W
        W += 1
        
print(ans)