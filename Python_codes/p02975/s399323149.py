n = int(input())
a = list(map(int, input().split()))
b = {}
for i in range(n):
    b[a[i]] = b[a[i]]+1 if a[i] in b else 1
b = list(b.items())
if len(b) == 1:
    print("Yes") if b[0][0] == 0 else print("No")
elif len(b) == 2:
    b.sort()
    print("Yes") if b[0][0] == 0 and b[0][1]*2 == b[1][1] else print("No")
elif len(b) == 3:
    print("Yes") if b[0][0]^b[1][0]^b[2][0] == 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1] else print("No")
else:
    print("No")