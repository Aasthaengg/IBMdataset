n,m = map(int, input().split( ))
cnt = [0]*n
#出現奇数回は不可
#出現偶数回なら勝手になる
for i in range(m):
    ai,bi = map(int, input().split( ))
    ai-=1;bi-=1
    cnt[ai]+=1;cnt[bi]+=1

for i in range(n):
    if cnt[i]%2:
        print("NO")
        exit()
print("YES")