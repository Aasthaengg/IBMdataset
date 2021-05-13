S = input()
K = int(input())

ans = []
table ={}

for i in range(len(S)):
    for j in range(i, len(S)+1):
        if (j-i)>=6:
            break
        if i==j:
            s = S[i]
            if s in table:
                continue
            table[s] = 1
            ans.append(s)
            continue
        if S[i:j]=="":
            continue
        s = S[i:j]
        if s in table:
            continue
        table[s] = 1
        ans.append(s)

ans = sorted(ans)
print(ans[K-1])
