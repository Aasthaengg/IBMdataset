N = int(input())
AB = []
for i in range(N):
    a,b = map(int,input().split())
    AB.append([a,b,a+b])

AB = sorted(AB, key=lambda x:x[2]*(-1))

A = 0
B = 0
for i in range(N):
    if i%2==0:
        A += AB[i][2]
    B += AB[i][1]
        
print(A-B)