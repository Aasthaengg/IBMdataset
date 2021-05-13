N = int(input())
ls = list(map(int,input().split()))
ls.sort(reverse=True)
a = 0
b = 0
for i in range(N):
    if i % 2 == 0:
        a += ls[i]
    else:
        b += ls[i]
print(a-b)