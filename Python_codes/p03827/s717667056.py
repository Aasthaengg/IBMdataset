n = int(input())
S = input()
Ans = [0]
ans = 0
for s in S:    
    if s == "I":
        ans += 1
    else:
        ans -= 1
    Ans.append(ans)

print(max(Ans))