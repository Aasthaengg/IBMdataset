
[X,Y] = list(map(int,input().split()))
out=0

i=X
while i<=Y:
    i=i*2
    out+=1
    # print('i,out:',i,out)
print(out)