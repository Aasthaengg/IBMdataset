N, C, K = map(int, input().split())
T = [0 for _ in range(N)]
for __ in range(N):
    T[__] = int(input())
 
T.sort()
bus_count = 1
bus_rest = C
bus_depert = T[0]+K
 
for ix in range(N):
 
    if T[ix] <= bus_depert and bus_rest > 0:
        bus_rest -= 1
 
    else:
        bus_count += 1
        bus_depert = T[ix] + K
        bus_rest = C - 1
 
print(bus_count)