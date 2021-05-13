import sys
N = int(input())
L = [i for i in range(1, N+1) if i % 2 != 0]
ans = 0
if N < 105:
    print(0)
    sys.exit(0)
for num in L:
    counter = 1
    for i in range(1, num//2):
        if num % i == 0:
            counter += 1
    if counter == 8:
        ans += 1
print(ans)