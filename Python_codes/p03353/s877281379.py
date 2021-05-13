#辞書順で一番小さいとこからK個つくる

s = input()
k = int(input())

early = list(set(s))
early.sort()


kouho = {}

for i in early:
    for j in range(len(s)):
        if s[j]==i:
            for l in range(k):
                kouho[s[j:j+l+1]]=0
    if len(kouho)>k:
        break

ans=list(kouho)
ans.sort()
print(ans[k-1])
