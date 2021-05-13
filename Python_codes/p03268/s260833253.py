N, K = list(map(int, input().split()))

if K==1:
    print(N**3)
    exit()
# if K==2:
#     print( ((N+1)//2)**3 +((N//2)**3))
#     exit()
if not K%2 == 0:
    print((N//K)**3)
    exit()

# print(N/K)
print((N//K)**3 +(int(N/K + 1/2)**3))