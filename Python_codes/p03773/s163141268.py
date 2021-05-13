time = input().split()

time_i = [int(s) for s in time]

t = time_i[0] + time_i[1]

if(t <= 23):
    print(t)
else:
    print(t-24)