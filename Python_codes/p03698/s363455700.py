S = list(input())
dic = {}

ans = True
for i in range(len(S)):
    if S[i] in dic:
        ans=False
        break
    else:
        dic[S[i]]=0

print("yes" if ans else "no")