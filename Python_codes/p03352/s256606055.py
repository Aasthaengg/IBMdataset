X = int(input())
l=[]
for i in range(1,101):
    for j in range(2,11):
        if i**j > 1000:
            break
        else:
            l.append(i**j)
for k in range(X):
    if X - k in l:
        print(X-k)
        break