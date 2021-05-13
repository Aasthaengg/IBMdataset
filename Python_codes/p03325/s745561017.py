import numpy
N = int(input())
a = numpy.array(list(map(int, input().split())))
count = 0

for i in range(N):
    if a[i] % 2 == 0:
        x = a[i]
        while True:
            if x %2 != 0:
                break
            else:
                x = x/2
                count+=1
print(count)