n = int(input())
t,a = [int(i) for i in input().split()]

h = [int(i) for i in input().split()]

cand = float('inf')
ans = 1

for i in range(n):
    temp = abs(a - (t - 0.006*h[i]))
    if cand > temp:
        cand = temp 
        ans = i+1
        
print(ans)