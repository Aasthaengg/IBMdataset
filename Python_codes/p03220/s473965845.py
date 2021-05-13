N=int(input())
T,A = list(map(int,input().split()))
H = list(map(int,input().split()))
delta_T = 700
ind  = 0
for i in range(N):
    if abs(T-H[i]*0.006 -A) < delta_T:
        delta_T = abs(T-H[i]*0.006 -A)
        ind = i
print(ind+1)
