N = int(input())
v = list(map(int, input().split()))
v.sort()

while len(v) > 1:
    v[1] = (v[0] + v[1])/2
    del v[0]

print(v[0])
