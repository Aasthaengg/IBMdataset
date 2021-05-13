n = int(input())
s = input()

ans = 0
for i in range(1,n-1):
    mae = s[:i]
    ato = s[i:]
    temp = []
    for j in mae:
        if j in ato:
            temp.append(j)
    temp = set(temp)
    ans = max(ans,len(temp))

print(ans)