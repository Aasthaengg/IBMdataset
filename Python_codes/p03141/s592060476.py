N = int(input())
l = []
for i in range(N):
    a,b = map(int,input().split())
    l.append((a+b,a,b))
l.sort(reverse=True)
A,B = 0,0
for i in range(N):
    if i%2 == 0:
        A += l[i][1]
    else:
        B += l[i][2]
print(A-B)