n = int(input())
X = input()

cnt = [0]*(200001)
for i in range(1,200001):
    pc = bin(i).count('1')
    cnt[i] = cnt[i%pc] + 1
    
plus = X.count("1")+1
minus = X.count("1")-1

defp = int(X, 2)%plus
if minus:
    defm = int(X, 2)%minus
else:
    defm = None

pl = 1
mi = 1
ans = []
for i, x in enumerate(X[::-1]):
    if x == "0":
        ans.append(cnt[(defp+pl)%plus]+1)
    else:
        if minus:
            ans.append(cnt[(defm-mi)%minus]+1)
        else:
            ans.append(0)
    pl = 2*pl%plus
    if minus:
        mi = 2*mi%minus

print(*ans[::-1], sep="\n")