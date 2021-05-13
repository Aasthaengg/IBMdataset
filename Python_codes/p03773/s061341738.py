t1, t2 = map(int, input().split())

t_start = (t1 + t2) % 24
print(t_start)