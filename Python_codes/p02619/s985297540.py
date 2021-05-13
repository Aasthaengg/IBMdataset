import numpy


d = int(input())
c = numpy.array(list(map(int, input().split())))
s = []
for i in range(d):
    s.append(list(map(int, input().split())))

result = []
past = numpy.array([0] * 26)
ans = 0
for i in range(d):
    past += 1
    t = int(input())
    past[t-1] = 0
    ans += sum(past * -c) + s[i][t-1]
    print(ans)
