# input the number for array of a[]
n = int(input())
a = list(map(int, input().split()))

# input the number for array of b[]
m = int(input())
b = list(map(int, input().split()))

# do the linear search
count = 0
for i in range(m):
    for j in range(n):
        if(b[i] == a[j]):
            count += 1
            break

print(count)

