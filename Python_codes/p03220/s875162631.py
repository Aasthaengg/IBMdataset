N = int(input())
T, A = map(int,input().split())
H = list(map(int, input().split()))

n = 0
t_best = 100000
for i in range(N):
    if abs(A - (T-H[i]*0.006)) < t_best:
        t_best = abs(A - (T-H[i]*0.006))
        n = i+1
    
print("{}".format(n))