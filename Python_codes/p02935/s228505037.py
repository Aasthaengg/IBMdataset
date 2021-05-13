n = int(input())
v = sorted(list(map(int,input().split())))

val = v[0]

for i in range(1,n):
    val += v[i]
    val /= 2
print(val)