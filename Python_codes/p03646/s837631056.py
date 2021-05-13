K = int(input())

mul = K//50
red = K%50

lis = [49+mul]*50
for i in range(red):
    lis[i] += 51
    for j in range(50):
        lis[j] -= 1

print(50)
print(*lis)