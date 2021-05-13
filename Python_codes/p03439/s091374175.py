# 1  2   3  4   5   6     7   8  9 
# 男　女　男　女　男　（空）　女　男　女
# 1が男であれば、奇数は男になるが、それが入れ替わる点を探す
# 0 〜 N-1　を二分探索
# midが0と同じ性別であれば、分岐点はmid〜N-1にある
# 違う性別であれば分岐点は0〜midにある

N=int(input())

print(0,flush = True)
point0 = input()

if point0 == "Vacant":
  exit(0)

print(N-1,flush = True)
if input() == "Vacant":
  exit(0)
  
left = 0
right = N-1
while True:
  mid = abs(left + right) // 2
  print(mid,flush = True)
  val = input()
  if val == "Vacant":
    exit(0)
  if (mid%2 == 0 and point0 == val) or (mid%2 == 1 and point0 != val):
    left = mid
  else:
    right = mid
