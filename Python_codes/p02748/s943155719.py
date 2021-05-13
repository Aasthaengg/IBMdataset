
A,B,M =map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
x = []
for m in range(M):
    x.append([int(i) for i in input().split()])
_min = min(a)+min(b)
		
for i in x:
    _min = min( (a[i[0]-1]+b[i[1]-1] - i[2]),_min)
print(_min)