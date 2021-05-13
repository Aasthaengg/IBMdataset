k = int(input())

l = [(k//50)+49]*50
if k%50:
    for i in range(k%50):
        l[i] += 51-k%50
    for j in range(k%50, 50):
        l[j] -= k%50

print(50)
print(*l)