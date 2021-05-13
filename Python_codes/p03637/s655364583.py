N = int(input())
A = [int(x) for x in input().split()]

x4 = 0
x2 = 0
x0 = 0
for a in A:
    if a % 4 == 0:
        x4 += 1
    elif a % 2 == 0:
        x2 += 1
    else:
        x0 += 1

if x2==0:
    if x4 >= x0 - 1:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    if x4 >= x0:
        ans = 'Yes'
    else:
        ans = 'No'
print(ans)