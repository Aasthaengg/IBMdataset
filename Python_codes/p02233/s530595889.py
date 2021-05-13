n = int(input())
f = [0]*45

f[0] = f[1] = 1
for i in range(2, 45):
    f[i] = f[i-2] + f[i-1]

print(f[n])
