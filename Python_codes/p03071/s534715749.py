a,b = map(int,input().split())
l = [a,b,a-1,b-1]
l.sort(reverse=1)
print(l[0]+l[1])