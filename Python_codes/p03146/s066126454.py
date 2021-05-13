s = int(input())

f = [s]

for i in range(1,1000000):
    if f[i-1] % 2 == 0:
        f.append(f[i-1]//2)
    else:
        f.append(3*f[i-1] + 1)
        
    for j in range(len(f)-1):
        if f[i] == f[j]:
            print(i + 1)
            exit()