N = int(input())

"""
N = 2
 No
N = 3
 1,2. 2,3. 3,1
N = 4
 No
N = 5
 No
N = 6
 1,2,4 1,3,6 4,5,6 2,3,5

個数がN(Nー1)でしょうと言うのは考察を諦めない力
全ての部分集合の長さって同じじゃね？って気付けるかどうか。。。
あとは６で具体的に構築できるかどうか勝負かな。
"""

def solve(k):
  print("Yes")
  print(k)
  G = []
  for i in range(1,k+1):
    G = calcG(i-1,G)
  for g in G:
    print(str(len(g)) + " " + " ".join(map(str,g)))
    
def calcG(i,G):
  st = i*(i-1) // 2 + 1
  en = i*(i+1) // 2
  #print(i,st,en)
  new = list(range(st,en+1))
  for j in range(len(G)):
    G[j].append(new[j])
  G.append(new)
  return G

for i in range(2,1000):
  if i*(i-1)//2 == N:
    solve(i)
    exit(0)

print("No")