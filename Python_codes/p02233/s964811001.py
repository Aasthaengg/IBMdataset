F = [1,1]
for i in range(2, int(input())+1):
    F.append(F[i-2] + F[i-1])
print(F[-1])