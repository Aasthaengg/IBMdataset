n = int(input())
d1 = []
d2 = []
for _ in range(n):
    a1,a2 = map(int,input().split())
    d1.append(a1)
    d2.append(a2)
count = 0
for i in range(n):
    if d1[i] == d2[i]:
        count += 1
    else:
        count = 0
    if count == 3:
        print("Yes")
        exit(0)
print("No")