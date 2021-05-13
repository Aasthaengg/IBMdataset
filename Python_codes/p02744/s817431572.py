"""
DFSを実装する.再帰を計算する必要があるので，関数の定義が必要
a - a -a
      -b
  - b -a
      -b
      -c
"""
N=int(input())
a_uni = ord('a')
z_uni = ord('z')
def dfs(s,maximum_uni):
    if len(s)==N:
        print(s)
        return None
    for i in range(a_uni,(maximum_uni+1)+1):
        maximum_uni = max(maximum_uni,i)
        dfs(s+chr(i),maximum_uni)
dfs('a',a_uni)


