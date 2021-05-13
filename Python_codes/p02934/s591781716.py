# 138 B

def inverse(y):
    return (1/y)

n = int(input())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += inverse(a[i])
print(inverse(sum))