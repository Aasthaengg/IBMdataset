
lst_1 = input().split()

A = int(lst_1[0])
B = int(lst_1[1])

if B%A == 0:
    ans = A + B
else:
    ans = B - A

print(ans)