n = int(input())
dishes = []
for i in range(n):
    ai,bi = map(int,input().split())
    dishes.append((ai,bi,ai+bi))
dishes.sort(key = lambda x:x[2],reverse = True)
A = 0
B = 0
for i in range(n):
    if i % 2 == 0:
        A += dishes[i][0]
    else:
        B += dishes[i][1]
print(A-B)