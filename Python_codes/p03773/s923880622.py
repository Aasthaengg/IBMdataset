A, B = map(int, input().split())

time_r = A + B
time = 0

if time_r >= 24:
    time = time_r - 24
else:
    time = time_r

print(time)
