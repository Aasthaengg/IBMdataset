#-------------
N = int(input())
#-------------

if N%2 == 0:
  k = N//2
else:
  k = (N+1)//2

cmb = []
for i in range(1,k+1):
  cmb.append([i , N-i])
  
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

ans = []
for i in range(k-1):
  X = digitSum(cmb[i][0])
  Y = digitSum(cmb[i][1])
  ans.append(X+Y)


if ans == []:
  print("2")
else:
  print(min(ans))