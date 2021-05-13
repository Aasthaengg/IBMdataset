n = int(input())
a = list(map(int, input().split()))
ave = sum(a) / n
b = [abs(ave - a[i]) for i in range(n)]
x = min(b)
for i in range(n):
    if b[i] == x:
        print(i)
        exit()