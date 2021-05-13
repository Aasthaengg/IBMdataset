N, K, L = map(int, input().split())

class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def root(self, A):
        if self.parent[A] == A:
            return A
        self.parent[A] = self.root(self.parent[A]) #経路縮約
        return self.parent[A]

    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)
        self.parent[A] = B
        
uni1 = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    if uni1.root(p-1) != uni1.root(q-1):
        uni1.connect(p-1,q-1)

uni2 = UnionFind(N)
for _ in range(L):
    r, s = map(int, input().split())
    if uni2.root(r-1) != uni2.root(s-1):
        uni2.connect(r-1,s-1)

# print (uni1.parent)
# print (uni2.parent)

ans = dict()
key_list = []
for i in range(N): #各都市を検索
    root1 = uni1.root(i) #都市の親を探す
    root2 = uni2.root(i)
    key = str(root1) + '_' + str(root2) #2つの親を連結したものをkeyとする
    key_list.append(key) #リストにkeyを足しておく(=i番目の都市が属するグループとして前からメモ)
    if key in ans.keys(): #dict andに親の組を記録していく
        ans[key] += 1
    else:
        ans[key] = 1
    
for i in range(N):
    print (ans[key_list[i]], end = ' ') #i番目の都市の親の組はkeyで読み出せる
print ()






# for i in range(1, N+1):
#     ans = 0
#     for j in range(1, N+1):
#         # print (uni1.root(i), uni1.root(j), uni2.root(i), uni2.root(j))
#         if uni1.root(i) == uni1.root(j) and uni2.root(i) == uni2.root(j):
#             ans += 1
#     print (ans, end = ' ')
print ()

# print (uni1.parent)
# print (uni2.parent)
