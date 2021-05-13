A,B=map(int,input().split())
H=[0]*1000

i=1
while i<=999:
    H[i]=i+H[i-1]
    i+=1

print(H[B-A]-B)