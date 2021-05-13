n = int(input())
v = sorted(list(map(int,input().split())))

for _ in range(n-1):
    x = v[0]
    y = v[1]
    num = (x+y)/2
    del v[0]
    v[0] = num

print(v[0])