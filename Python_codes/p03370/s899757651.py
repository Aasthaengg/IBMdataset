n,x = map(int,input().split())
gram = []
for i in range(n):
    gram.append(int(input()))
    x -= gram[i]
gram.sort(key=int)
print(n + (x // gram[0]))