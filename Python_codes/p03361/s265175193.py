h,w=map(int,input().split())
lista=[]
ans=0
count=0
for i in range(h):
    lista.append(list(input()))
for i in range(h):
    for j in range(w):
        count=0
        if lista[i][j]=="#":
            if i!=0:
                if lista[i-1][j]=="#":
                    count=1
            if j!=0:
                if lista[i][j-1]=="#":
                    count=1
            if i!=h-1:
                if lista[i+1][j]=="#":
                    count=1
            if j!=w-1:
                if lista[i][j+1]=="#":
                    count=1
            if count==0:
                ans=1
                break
    if ans==1:
        break
if ans==1:
    print("No")
else:
    print("Yes")
