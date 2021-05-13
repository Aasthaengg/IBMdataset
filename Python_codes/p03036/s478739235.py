R,D,X=map(int, input().split())
Plus=X
for i in range(10):
    print((Plus*R)-D)
    Plus=((Plus*R)-D)