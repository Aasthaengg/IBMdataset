N = int(input())
count = 0
for i in range(N):
    if N==0:
        break
    if N%10 == 2:
        count += 1
    N //= 10

print(count)