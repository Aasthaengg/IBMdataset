def main():
    N = int(input())
    # cnt[a][b] := 先頭がa,末尾がqである数の個数
    cnt = [[0]*10 for i in range(10)]
    for i in range(1,N+1):
        s = str(i)
        cnt[int(s[0])][int(s[-1])] += 1
    ans = 0
    for a in range(10):
        for b in range(10):
            ans += cnt[a][b]*cnt[b][a]
    print(ans)

main()
