N = int(input())
A_arr = [int(x) for x in input().split()]

A_max = max(A_arr)
A_min = min(A_arr)

ans_arr = []
if A_max > -A_min:
    Am = A_arr.index(A_max)
    for i in range(len(A_arr)):
        if i == Am:
            continue
        ans_arr.append((Am+1, i+1))
    for i in range(len(A_arr)-1):
        ans_arr.append((i+1, i+2))
else:
    Am = A_arr.index(A_min)
    for i in range(len(A_arr)):
        if i == Am:
            continue
        ans_arr.append((Am+1, i+1))
    for i in range(len(A_arr)-1, 0, -1):
        ans_arr.append((i+1, i))

print(len(ans_arr))
for i,j in ans_arr:
    print(i,j)

