K = int(input())

extra = 7 % K

#あまり0と出会う前にが同じあまりのものと合うと終わりなのでそれをチェック。
seen = set()
ans = 1

while extra not in seen:
    if extra == 0:
        print(ans)
        exit()
    seen.add(extra)
    extra = (extra*10 + 7) % K
    ans += 1
print(-1)    