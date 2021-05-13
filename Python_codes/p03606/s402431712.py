N = int(input())
l = [input().split() for i in range(N)] #二次元リストを生成
ans = 0
for j in l:
    num = int(j[1]) - int(j[0]) + 1
    ans += num
print(ans)
