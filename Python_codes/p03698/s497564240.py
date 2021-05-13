S = list(input()) #１文字ずつ
N = len(S)

cnt=[0]*26
al = [chr(ord('a') + i) for i in range(26)]
for i in range(N):
    for j in range(26):
        if S[i] == al[j]:
            cnt[j]+=1
# print(cnt)

out='yes'
for i in range(26):
    if cnt[i]>=2:
        out='no'

print(out)
