k = int(input())

size = 50
l = [(k//size)+size-1]*size
if k%size:
    for i in range(k%size):
        l[i] += size-(k%size-1)
    for j in range(k%size, size):
        l[j] -= k%size

print(size)
print(*l)