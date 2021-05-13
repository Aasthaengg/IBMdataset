N = int(input())
S = list(input())
ans = 0
temp =[0]
for i in range(N):
    if S[i] == "I":
        ans += 1
        temp.append(ans)
    elif S[i] == "D":
        ans-=1
        temp.append(ans)
print(max(temp))