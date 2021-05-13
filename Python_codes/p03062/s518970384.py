n = int(input())
li = list(map(int,input().split()))
x = 0

for i in range(n):
    if li[i] < 0:
        li[i] *= -1
        x += 1

if x%2 == 0:
    print(sum(li))
else:
    print(sum(li)-min(li)*2)