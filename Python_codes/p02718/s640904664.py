# ABC161
# B Popular Vote
N, M = map(int, input().split())  # N種類　M個選ぶ
a = sorted(list(map(int, input().split())),reverse=True)
x = sum(a)
q = x / (4 * M)
b =[]
for i in range(M):
    b.append(a[i])
b = sorted(b)
for j in b:
    if j < q:
        print('No')
        exit()
print('Yes')
