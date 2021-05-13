import numpy
H, W, M = [int(x) for x in input().split()]

width = numpy.array([0] * W, dtype='int64')
height = numpy.array([0] * H, dtype='int64')

obj = set()
for i in range(M):
    h, w = [int(x) - 1 for x in input().split()]

    width[w] += 1
    height[h] += 1
    obj.add((h, w))

result_h = set(numpy.where(height == numpy.max(height))[0])
result_w = set(numpy.where(width == numpy.max(width))[0])

if len(result_h) * len(result_w) > M:
    print(numpy.max(height) + numpy.max(width))
    exit()

for h in result_h:
    for w in result_w:
        if not (h, w) in obj:
            print(numpy.max(height) + numpy.max(width))
            exit()

print(numpy.max(height) + numpy.max(width) - 1)
