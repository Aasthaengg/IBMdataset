l = list(map(int,input().split()))
k = int(input())
L =l.sort()
print(l[0]+l[1]+l[2]*(2**k))
