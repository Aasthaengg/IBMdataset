def find(x):#xの親を見つける
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x,y):#要素xとｙを併合させる
  x,y=find(x),find(y)#xとyの親の検索
  if x!=y:#親が異なる場合併合させる
    if x>y:
        x,y=y,x#小さい方をxとする. これにより要素の値が小さいものを優先して木の根とする. 
    par[x]+=par[y] #値を無向木の要素数の和にする.
    par[y]=x #枝側は根の位置を格納

def same(x, y):#要素xと要素yが同じ無向木に所属しているかを判定する
  return find(x) == find(y)#同じ値を持つか否か

def size(x):#要素xが所属する無向木の大きさを返す
  return-par[find(x)]

par = [-1] * 200005#parは木の根の情報を持つ配列, xが根元ならpar[x]はその無向木に所属する要素の数を, そうでない場合は所属する根元のparにおける位置を示す数値が格納される. 


def main():
  n, m = map(int, input().split())
  for i in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)
  print(abs(min(par)))
  
if __name__ == "__main__":
  main()