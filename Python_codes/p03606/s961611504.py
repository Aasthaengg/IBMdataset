n = int(input())
c = [0]*10**5
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        c[j-1] = 1
print(sum(c))
