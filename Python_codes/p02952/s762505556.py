N = int(input())
   
count = 0
for n in range(0, N+1):
    if 1 <= n <= 9:
        count = count + 1
    if 100 <= n <= 999:
        count = count + 1
    if 10000 <= n <= 99999:
        count = count + 1
print(count)