n, a, b = map(int, input().split())
result = 0
if (b - a)%2 == 1:
    temp1 = a - 1
    temp2 = n - b
    work = temp1 if temp1 < temp2 else temp2
    if (b-a)//2 == 1:
        result = work
    else:
        result = work + 1 + (b-a-1)//2
else:
    result = (b - a) // 2
print(result)