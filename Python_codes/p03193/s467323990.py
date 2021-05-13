n, h, w = map(int, input().split())
cutable = []
for i in range(n):
    a, b = map(int, input().split())
    if h<=a and w<=b:
        cutable.append(i)
print(len(cutable))
