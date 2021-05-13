N,M = map(int,input().split())
H = list(map(int,input().split()))
List = [0]*N
for i in range(M):
    A,B = map(int,input().split())
    if(H[A-1] > H[B-1]):
        List[B-1] = 1
    elif(H[A-1] < H[B-1]):
        List[A-1] = 1
    else:
        List[A-1] = 1
        List[B-1] = 1
print(str(List.count(0)))