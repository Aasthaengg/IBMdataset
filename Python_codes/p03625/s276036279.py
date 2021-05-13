N = int(input())
A = list(map(int, input().split()))

useable = []
memo = {}

for a in A:
    try:
        memo[a] += 1
    except:
        memo[a] = 1
    if memo[a] == 2:
        useable.append(a)
        memo[a] = 0

# print(useable)

if len(useable) < 2:
    print(0)
else:
    useable.sort()
    print(useable[-1] * useable[-2])
