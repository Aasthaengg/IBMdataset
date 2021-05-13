n = int(input())
h = list(map(int,input().split()))
q = [0]*n
for i in range(n):
    q[h[i]-1] = i+1
print(*q)