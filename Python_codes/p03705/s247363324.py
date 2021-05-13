N,A,B = map(int,input().split())
X = A*(N-1)+B
Y = A+B*(N-1)
print(max(Y-X+1,0))