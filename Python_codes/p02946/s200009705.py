k, x = map(int, input().split())

l = k*2 -1

m = x - k + 1

for i in range(l):
    print(i+m, end = " ")
