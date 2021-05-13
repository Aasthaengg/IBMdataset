n = int(input())
a = input().split()

for i in range(1, n):
    print(str(a[-i]) + " ", end = "")
print(a[0])