n, hp = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
mat.sort(key=lambda x:-x[1])
sword = max(mat, key=lambda x:x[0])[0]
s, t = mat[0]
idx = 0
ans = 0
for _, throw in mat:
    if throw > sword:
        hp -= throw
        ans += 1
        if hp <= 0:
            print(ans)
            exit()
    else:
        break
d, m = divmod(hp, sword)
ans += d + min(1, m)
print(ans)
