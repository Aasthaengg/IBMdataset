#aからｂの整数。
a,b = map(int,input().split())
count=0
for i in range(a,b+1):
    i = str(i)
    if i == i[::-1]:
        count +=1
    else :
        pass
print(count)


