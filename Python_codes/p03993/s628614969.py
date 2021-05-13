n = int(input())
a = [int(x) for x in input().split()]

# print(a)

# print(n)
# print(a)
count = 0


for i in range(n + 1):
    if(i == a[a[i - 1] - 1]):
        count += 1


print(int(count/2))
