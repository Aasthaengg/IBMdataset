n = int(input())
a = list(map(int,input().split()))
flag = 1
count = 0
while flag:
    flag = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count += 1
            flag = 1
print(" ".join(map(str,a)))

print(count)