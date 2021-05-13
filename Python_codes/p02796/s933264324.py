n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
st_en = [[x-l, x+l] for x, l in xl]

st_en.sort(key=lambda x: x[1])

now = -10**9+10
ans=0
for st, en in st_en:
    if now <= st:
        now = en
        ans+=1
print(ans)