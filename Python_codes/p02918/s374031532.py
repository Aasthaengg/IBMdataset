n,k = map(int,input().split())
S = input()

C = []

count = 0
dotti = S[0]
ans = 0

for i in range(n):
    if dotti != S[i]:
        count += 1
        dotti = S[i]
    if S[i] == "R" and i < n-1: 
        if S[i+1] == "R":
            ans += 1
    elif S[i] == "L" and i > 0: 
        if S[i-1] == "L":
            ans += 1

while k > 0:
    if count >= 2:
        ans += 2
        count -= 2
    elif count == 1:
        ans += 1
        count -= 1
        break
    else:
        break
    k -= 1

print(ans)