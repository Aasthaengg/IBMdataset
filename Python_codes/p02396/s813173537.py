a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
for i in range(len(a)):
    print("Case", str(i+1) + ":", a[i])