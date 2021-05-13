N = int(input())
num,a = 0,0
l = []
for i in range(N):
    num += 1
    a += num
    l += num,
    if a >= N:
        minus = a - N
        break

for i in l:
    if i != minus:
        print(i)