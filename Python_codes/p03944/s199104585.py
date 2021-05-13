w,h,n = map(int,input().split())
x = [0] * n
y = [0] * n
a = [0] * n
for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())
box = []

for i in range(h):
    box.append([1]*w)
for i in range(n):
    if a[i] == 1:
        for m in range(h):
            for j in range(x[i]):
                box[m][j] = 0  
    elif a[i] == 2:
        for m in range(h):
            for j in range(x[i],w):
                box[m][j] = 0
    elif a[i] == 3:
        for m in range(y[i]):
            for j in range(w):
                box[m][j] = 0
    else:
        for m in range(y[i],h):
            for j in range(w):
                box[m][j] = 0
print(sum(map(sum,box)))