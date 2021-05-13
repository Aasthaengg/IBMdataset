#n, m, q = map(int, input().split())
#List = list(map(int, input().split()))
#req = [list(map(int, input().split())) for _ in range(q)]
#t = t[:-1]
#print(ans[j], end = "") 改行無しで出力
#[0]*n
n, m = map(int, input().split())

g = n*(n-1)/2
k = m*(m-1)/2

print(int(g+k))
