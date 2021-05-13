n = int(input()) 
v = list(map(int, input().split()))
c = list(map(int, input().split()))

max_diff_v_c = 0
for i in range(n):
    diff_v_c = v[i] - c[i]
    if diff_v_c > 0:
        max_diff_v_c += diff_v_c

print(max_diff_v_c)