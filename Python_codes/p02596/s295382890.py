k = int(input())

a = [7%k]

for i in range(1, k):
    a.append((a[i-1]*10+7)%k)

for i in range(k):
    if a[i] == 0:
        print(i+1)
        exit()

print(-1)