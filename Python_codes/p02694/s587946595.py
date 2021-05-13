x = int(input())
p = 100
t , si= 0, 0
while(p < x):
    si = p//100
    p += si
    t += 1
print(t)

