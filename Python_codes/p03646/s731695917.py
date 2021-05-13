K = int(input())

N0 = K % 50
A = K//50+49
a = [0] * 50

for i in range(0,50-N0):
    a[i] = A - N0
for i in range(50-N0,50):
    a[i] = A - N0 + 51

print(50)
print(" ".join(list(map(str,a))))