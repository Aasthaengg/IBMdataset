N = int(input())
v = sorted(list(map(int,input().split())),reverse=True)
val = 0
for i in range(N):
    val += v[i]/(2**(i+1))
val += v[N-1]/(2**N)
print(val)
