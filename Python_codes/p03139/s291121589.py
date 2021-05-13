N,A,B = (int(x) for x in input().split())
if(A<B):
    max = A
else:
    max = B

min = A+B
if(min>N):
    min = min - N
else:
    min = 0

print(max,min)