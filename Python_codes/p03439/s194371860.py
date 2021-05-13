N= int(input())

# queryを投げて空の時の処理をする関数
def query1(i):
  print(i)
  tmp = input()
  if tmp[0] == 'V':
    exit()
  return tmp

# 最初に始点を探索
z = query1(0)
  
# 矛盾していないか判定する関数, Falseなら矛盾
def judge1(m):
  s = query1(m)
  if m % 2 == 0: # 偶数なら0番目と同じなら矛盾しない
    return z==s
  else:
    return z!=s
  
# 二分探索する
l = 0
r = N # N-1にするとN-1が探索されずにwhileを抜けてしまう
while r - l > 1:
  m = (l + r) // 2
  if judge1(m):
    # l~mまでが矛盾しない
    l = m
  else:
    r = m