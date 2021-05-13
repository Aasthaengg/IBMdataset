N,A,B=list(map(int,input().split()))

maximum=min(A,B)
if N>A+B:
    minimum=0
else:
    minimum=A+B-N

print(str(maximum)+' '+str(minimum))