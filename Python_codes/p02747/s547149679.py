S = input()
#a,b = map(int,input().split())

ans = "Yes"
if len(S) % 2 == 1:
    ans = "No"

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] != "h":
            ans = "No"
    else:
        if S[i] != "i":
            ans = "No"

print(ans)