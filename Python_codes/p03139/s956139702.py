N,A,B = map(int,input().split())
ma = min(A,B)
mi = A+B-N
if mi<=0:
    mi = 0
print(ma,mi)