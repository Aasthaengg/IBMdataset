


X,Y,Z,K = map(int, input().split())
A = list( map(int, input().split()))
B = list( map(int, input().split()))
C = list( map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


"""
愚直解
X*Y*Z全部作って上から順にK個書き出す。普通に間に合わない
愚直解のいけてない部分として、X*Yを作った段階で、他のX*Yよりずっと小さいときに、Zとの積を見るまでもなくK番目までに入らないケースがある。
なんというか、　X*Y*Z　を　W*Z (W=X*Y)と置き換えたときに、Wの中で順位が低いものとZとの積を計算して他と比較する意味がない。
W = [9,8,7,6,5,4,3]
Z = [6,4,3,2,1]
K = 5
とかで考えると、Wが3や4のものは見る必要がない。
というのも、それより大きいWがK個以上あることが分かっているので、W*ZもK個以上大きいものが存在するといえるので。

なので、先にX*Yを計算して、その中で上位K個とZの積をとってさらにK個選べばいけそう


"""
W = []
for a in A:
    for b in B:
        W.append(a+b)

W.sort(reverse=True)
if len(W) > K:
    W = W[:K]
ans = []
for w in W:
    for c in C:
        ans.append(w+c)

ans.sort(reverse=True)
print(*ans[:K], sep="\n")