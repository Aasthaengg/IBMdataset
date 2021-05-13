n=int(input())
a=[int(input()) for _ in range(n)]
max_a=max(a)
index=a.index(max_a)
a.pop(index)
for i in range(n):
    if i ==index:
        print(max(a))
    else:
        print(max_a)