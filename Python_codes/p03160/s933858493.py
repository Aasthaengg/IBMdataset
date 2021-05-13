n = int(input())
h_l = list(map(int, input().split()))
m = [0] * n
m[0] = 0
m[1] = abs(h_l[1] - h_l[0])
for i in range(2, n):
    m[i] = min(m[i-1] + abs(h_l[i] - h_l[i-1]), m[i-2] + abs(h_l[i] - h_l[i-2]))
print(m[-1])