
def limpstr():return list(map(str,input().split()))

l=limpstr()
l.sort(reverse=True)
print(int(l[0]+l[1])+int(l[2]))
