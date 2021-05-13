u = []
time = 0
for i in range(5):
    s = int(input())
    t = ((s+ 9) // 10) * 10
    u.append(t - s)
    time += t
    
print(time - max(u))