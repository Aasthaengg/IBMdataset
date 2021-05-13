a,b,c = map(int,input().split())

lists = [a,b,c]

x = max(lists)

lists.remove(x)

y = max(lists)

lists.remove(y)

print(int(abs(y-x)) + int(abs(lists[0] - y))) 

