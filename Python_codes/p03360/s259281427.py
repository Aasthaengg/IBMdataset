l = list(map(int,input().split()))
k = int(input())
L =l.sort()
print(int(l[0])+int(l[1])+int(l[2])*(2**k))
