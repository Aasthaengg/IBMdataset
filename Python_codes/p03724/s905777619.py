n, m = map(int, input().split())
vertex_dic = {}
def add_dic(p):
    if not p in vertex_dic:
        vertex_dic[p] = 1
    else:
        vertex_dic[p] += 1
for i in range(m):
    line = list(map(int, input().split()))
    add_dic(line[0])
    add_dic(line[1])
ans = "YES"
for key, item in vertex_dic.items():
    if item%2 == 1:
        ans = "NO"
print(ans)
