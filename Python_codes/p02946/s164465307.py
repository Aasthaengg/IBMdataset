k,x=input().split()
k=int(k)
x=int(x)

ls1=range(k+(k-1))
ls2=[n+(x-(k-1)) for n in ls1]
print(*ls2)