l=list(map(int,input().split()))
a = l[0]
b = l[1]
c = l[2]


print(max(c - (a-b), 0))
