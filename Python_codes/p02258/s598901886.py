N = int(input())
r = [int(input()) for i in range(N)]
 
min = r[0]
max = -9999999999999999
 
for i in range(1, N):
    if r[i] - min > max:
        max = r[i] - min
    if r[i] < min:
        min = r[i]
 
print(max)