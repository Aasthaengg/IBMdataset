line = input()
A, B, T = [int(n) for n in line.split()]
T+=0.5
i = 0
while A*(i+1) <= T:
    i+=1
print(i*B)