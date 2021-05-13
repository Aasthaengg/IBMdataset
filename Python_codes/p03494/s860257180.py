n = int(input())
a = list(map(int, input().split()))

two = [0] * n

for i in range(n):
        while a[i]%2 == 0 :
                two[i] += 1
                a[i] = a[i] / 2
print(min(two))