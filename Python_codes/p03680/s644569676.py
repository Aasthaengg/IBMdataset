n=int(input())
li=[int(input()) for i in range(n)]
basyo=1
res=-1
for i in range(2*n):
    basyo=li[basyo-1]
    if basyo==2:
        res=i+1
        break
print(res)