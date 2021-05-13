a, b = map(int,input().split())
tmp_start_time = a + b
start_time = 0
if tmp_start_time >= 24:
    start_time = tmp_start_time - 24
else:
    start_time = tmp_start_time
print(start_time)