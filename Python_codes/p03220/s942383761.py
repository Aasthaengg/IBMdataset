N = int(input())
T,A = map(int,input().split())
H = [int(n) for n in input().split()]

min_t = 10**5
min_i = 0

for i in range(N):
    t = abs(A - (T - H[i]*0.006))
    if t <= min_t:
        min_t = t
        min_i = i


print(min_i+1)