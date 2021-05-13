N = int(input())
a = list(map(int,input().split()))
b = []

for i in range(N):
    a_2 = 0
    while a[i]%2 == 0:
        a[i] = a[i]//2
        a_2 += 1
    b.append(a_2)
print(sum(b))
