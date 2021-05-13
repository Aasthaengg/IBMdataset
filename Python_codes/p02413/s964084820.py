y,x = map(int,raw_input().split())
list =[]
last = [ 0 for a in range(x+1)]

for a in range(y):
    tmp = map(int,raw_input().split())
    list.append(tmp + [sum(tmp)])
    for i,b in enumerate(list[a]):
        last[i] = last[i] + b

for c in list:
    print " ".join(map(str,c))
print " ".join(map(str,last))