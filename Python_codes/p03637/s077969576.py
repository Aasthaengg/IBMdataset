n = int(input())
a = list(map(int, input().split()))
a1, a2, a3 = [], [], []
for i in a:
    if i%4 == 0:
        a1.append(i)
    elif i%2 == 0:
        a2.append(i)
    else:
        a3.append(i)
if len(a2) > 0:
    if len(a1) >= len(a3):
        print("Yes")
    else:
        print("No")
else:
    if len(a1)+1 >= len(a3):
        print("Yes")
    else:
        print("No")