N = int(input())
MOD = 10**9+7
S = []
for i in range(2):
    t=[]
    s=input()
    for j in range(len(s)):
        t.append(s[j])
    S.append(t)
#i,jが一致するものと同じ色は使えない

l=[]
for i in range(N):
    if i>=1:
        if S[0][i]==S[0][i-1]:
            continue

    if S[0][i]==S[1][i]:
        l.append("x")
    else:
        l.append("y")
ans = 1

for i in range(len(l)):
    if i==0:
        if l[i]=="x":
            ans *= 3
        else:
            ans *= 6
        continue
    if l[i]=="x":
        if l[i-1]=="x":
            ans *= 2
        else:
            ans *= 1
    else:
        if l[i-1]=="x":
            ans *= 2
        else:
            ans *= 3
ans = ans%MOD
print(ans)