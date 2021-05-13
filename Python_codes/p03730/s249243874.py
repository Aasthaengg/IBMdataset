A,B,C = map(int,input().split())

dic = {}
tmp = A%B
while not(tmp in dic):
    dic[tmp]=0
    tmp = (tmp+(A%B))%B


print("YES" if C in dic else "NO")