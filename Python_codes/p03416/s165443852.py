A, B = map(int, input().split())
count = 0 
for i in range(A, B+1):
    num = str(i)
    judge = 1
    for j in range(len(num) // 2):
        if num[j] != num[-j-1]:
            judge = 0
            break
    if judge:
        count += 1

print(count)