A,B,N=map(int,input().split())

if N>=B-1:
    max_value=int(((B-1)/B)*A)
else:
    max_value=int((N/B)*A)

print(max_value)   