N,X = map(int,input().split())
L = list(map(int,input().split()))
l = [0]
for a in L:
    l.append(l[-1] + a)
print(len([1 for c in l if c <= X]))