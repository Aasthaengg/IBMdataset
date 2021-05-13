N,A,B = list(map(int,input().split()))
if N==1 and A!=B:
    print(0)
    exit()
elif A>B:
    print(0)
    exit()

min = B+A*(N-1)
max = B*(N-1)+A
print(max-min+1)