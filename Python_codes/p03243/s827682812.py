n = int(input())
for i in range(9):
    if n > 111*i and n <= 111*(i+1):
        ans = 111*(i+1)
        break
print(ans)