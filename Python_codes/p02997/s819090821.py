from itertools import combinations

# 自分の答案に組み込んで見る
a,b = map(int,input().split())

S  = (a-1)*(a-2)//2
def solve(x,y,s):
    print(a+s-y-1)
    for i in range(1,a):print(1,1+i)
    c = s-b
    edges = list(combinations(range(2, a+1), 2))[:c]
    for i, j in edges:
        print(i, j)
# print(b,S)
if not 0<= b <= S:
    print(-1)
    exit()
else:
    solve(a,b,S)
