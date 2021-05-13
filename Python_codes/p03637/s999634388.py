n = int(input())
list_A = list(map(int, input().split()))
list_C = [0, 0, 0]

for num in list_A:
    if num % 4 == 0:
        list_C[2] += 1
    elif num % 2 == 0:
        list_C[1] += 1
    else:
        list_C[0] += 1

ans = "Yes"

if list_C[1] == 0:
    if list_C[2] == 0:
        if list_C[0] != 0:
            ans = "No"
    if list_C[2] == 1:
        if list_C[0] > 2:
            ans = "No"
    if list_C[2] > 1:
        if list_C[0] > list_C[2] + 1:
            ans = "No"
else:
    if list_C[0] > list_C[2]:
        ans = "No"

print(ans)