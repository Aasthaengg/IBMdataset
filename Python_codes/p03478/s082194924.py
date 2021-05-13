N,A,B=list(map(int,input().split()))
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

ans=0
for i in range(1,N+1):
  S=digitSum(i)
  if A<=S<=B:
    ans+=i
print(ans)