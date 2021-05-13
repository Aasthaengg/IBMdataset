n, a, b = map(int, input().split())
v_max = min(n,a,b)
v_min = max(a+b-n, 0)
print(v_max, v_min)