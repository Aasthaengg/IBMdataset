S = input()
K = int(input())

ans = []
table ={}

for i in range(len(S)):
    for j in range(6):
        if i==j:
            s = S[i]
            if s in table:
                continue
            table[s] = 1
            ans.append(s)
            continue
        if S[i:i+j]=="":
            continue
        s = S[i:i+j]
        if s in table:
            continue
        table[s] = 1
        ans.append(s)

ans = sorted(ans)
print(ans[K-1])
