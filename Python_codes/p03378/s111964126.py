n,m,x = map(int, input().split())
al = list(map(int, input().split()))

res = sum(y < x for y in al)  # 真偽値リストを作って True の数を合計する方法
ress = m-res

print(min(res,ress))