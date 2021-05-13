import bisect
n = int(input())
l = list(sorted(map(int, input().split())))


'''
a,bの値を指定し、その合計値を下回る値の最大値のインデックス番号を取得
インデックス番号から指定していたb（大きい方の値）を引く
'''
ans = 0
for a in range(n):
  for b in range(a+1, n):
    ans += bisect.bisect_left(l, l[a]+l[b]) - (b+1)
print(ans)