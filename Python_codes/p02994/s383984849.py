n,l = map(int,input().split())

li = [x+l for x in range(n)]
if 0 in li:
    print(sum(li))
elif min(li) > 0:
    print(sum(li)-min(li))
else:print(sum(li)-max(li))