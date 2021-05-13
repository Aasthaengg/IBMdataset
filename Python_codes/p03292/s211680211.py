a,b,c = (int(x) for x in input().split())

list = []
list.append(abs(a-b)+abs(b-c))
list.append(abs(a-c)+abs(c-b))
list.append(abs(b-a)+abs(a-c))
print(min(list))
