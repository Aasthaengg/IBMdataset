N = list(input())
temp = 0
for n in N:
    k = int(n)
    temp += k
if temp % 9 == 0:
    print("Yes")
else:
    print("No")