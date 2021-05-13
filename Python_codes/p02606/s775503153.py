L,R,D=map(int,input().split())
startno = L
while startno % D != 0:
    startno += 1 
lista=list(range(startno,R+1,D))
#print(lista)
print(len(lista))