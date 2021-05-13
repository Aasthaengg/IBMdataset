N,K= map(int, input().split())
list = list(map(int, input().split())) #Hiを入力

list.sort()
if N>=K:
    while K>=1:
        del list[-1]
        K=K-1
else:
    list.clear()

x=0
for i in list:
    x=x+i

print(str(x))
