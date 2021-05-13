n = int(input())
num = list(map(int,input().split()))
a = 0
for i in range(n):
    for j in range(i + 1,n):
        a += num[i] * num[j]

print(a)