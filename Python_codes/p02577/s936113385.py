n = list(input())
b = int(n[0])
for a in range(len(n)-1):
    b = b + int(n[a+1])
if b % 9 == 0:
    print("Yes")
else:
    print("No")