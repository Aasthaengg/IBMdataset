h,w= [int(i) for i in input().split()]
x=[[int(0)for i in range(w)]for j in range(h)]
z=[int(0 ) for i in range(w)]
for i in range(h):
    y=[int(k) for k in input().split()]
    for s in range(w):
        x[i][s]=y[s]
for s in range(w):
    z[s]=int(input())
for i in range(h):
    count=0
    for s in range(w):
        count=count+x[i][s]*z[s]
    print(count)