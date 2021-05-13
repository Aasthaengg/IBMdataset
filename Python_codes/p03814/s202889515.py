din = str(input())
length = len(din)
first_A = -1
last_Z = -1
for i in range(length):
    if (din[i] == 'A' and first_A == -1):
        first_A = i
    elif din[i] == 'Z':
        last_Z = i
print(last_Z-first_A+1)
