n=int(input())
a,b=map(int,input().split())
p = [int(x) for x in input().split()]
A=0
B=0
C=0
for i in range(n):
    if p[i] <= a:
        A += 1
    elif p[i] > a and b >= p[i]:
        B += 1
    else:
        C += 1

print(min(A, B, C))