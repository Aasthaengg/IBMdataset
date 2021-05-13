a,b,c = map(int,input().split())

lis = [a,b,c]

lis.remove(max(lis))

print(int(lis[0]*lis[1]/2))
