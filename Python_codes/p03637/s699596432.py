N = int(input())
A = list(map(int, input().split()))
memo = {1:0,2:0,4:0}

for a in A:
    if a % 4 == 0:
        memo[4] += 1
    elif a % 2 == 0:
        memo[2] += 1
    else:
        memo[1] += 1

if memo[4] >= (N//2):
    print("Yes")
elif memo[4] >= memo[1]:
    print("Yes")
else:
    print("No")
