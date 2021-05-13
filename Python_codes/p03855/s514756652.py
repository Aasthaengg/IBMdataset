N, K, L=map(int, input().split())

R=[[] for i in range(N)]
T=[[] for i in range(N)]


class UnionFind():
  # 作りたい要素数nで初期化
  # 使用するインスタンス変数の初期化
  def __init__(self, n):
    self.n = n
    # root[x]<0ならそのノードが根かつその値が木の要素数
    # rootノードでその木の要素数を記録する
    self.root = [-1]*(n+1)
    # 木をくっつける時にアンバランスにならないように調整する
    self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
  def Find_Root(self, x):
    if(self.root[x] < 0):
      return x
    else:
    # ここで代入しておくことで、後の繰り返しを避ける
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]

    # 木の併合、入力は併合したい各ノード
  def Unite(self, x, y):
    # 入力ノードのrootノードを見つける
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    # すでに同じ木に属していた場合
    if (x == y):
      return 
      # 違う木に属していた場合rnkを見てくっつける方を決める
      #rnkが大きい方に結合
    elif (self.rnk[x] > self.rnk[y]):
      self.root[x] += self.root[y]
      self.root[y] = x

    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      # rnkが同じ（深さに差がない場合）は1増やす
      if(self.rnk[x] == self.rnk[y]):
        self.rnk[y] += 1

  # xとyが同じグループに属するか判断
  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)

  # ノードxが属する木のサイズを返す
  def Count(self, x):
    return -self.root[self.Find_Root(x)]

uniR=UnionFind(N)
for i in range(K):
  p,q=map(int, input().split())
  R[p-1].append(q-1)
  R[q-1].append(p-1)
  
  uniR.Unite(p-1,q-1)
uniT=UnionFind(N)  
for i in range(L):
  r, s=map(int, input().split())
  T[r-1].append(s-1)
  T[s-1].append(r-1)
  
  uniT.Unite(r-1,s-1)
dic = {}  
for i in range(N):
    val = (uniR.Find_Root(i), uniT.Find_Root(i))
    if val in dic:
        dic[val] += 1
    else:
        dic[val] = 1
        
for i in range(N):
    print(dic[(uniR.Find_Root(i), uniT.Find_Root(i))], end=" ")