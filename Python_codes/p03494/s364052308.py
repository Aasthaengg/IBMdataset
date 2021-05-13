n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    count = 0
    for j in reversed(bin(a[i])):
        if j == '0':
            count+=1
        else:
            break
    a[i] = count

print(min(a))