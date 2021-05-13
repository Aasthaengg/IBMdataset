l=list(map(str,input().split()))
l.sort(reverse=True)
print(int(l[0]+l[1])+int(l[2]))