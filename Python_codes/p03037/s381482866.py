N,M = map(int,input().split())
minimum = 1
maximum = N 
for i in range(M):
    L,R = map(int,input().split())
    minimum = max(minimum,L)
    maximum = min(maximum,R)
    if minimum > maximum:
        print(0)
        exit(0)

print(maximum - minimum + 1)