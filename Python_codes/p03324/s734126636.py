l = list(map(int, input().split()))
D = l[0]
N = l[1]
if N != 100:  
    answer = (100**D)*N
else:
    answer = (100**D)*(N+1)
print(answer)
