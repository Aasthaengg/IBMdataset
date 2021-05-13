n, k, c = map(int, input().split())
s = input()

foward = [0] * (k + 1)
backward = [0] * (k + 1)

# foward check
day = 1
i = 0
while i < n and 0 < day <= k:
    if s[i] == "o":
        foward[day] = i
        i += c
        day += 1
    i += 1

# backward check
day = k
i = n - 1
while 0 <= i and 0 < day <= k:
    if s[i] == "o":
        backward[day] = i
        i -= c
        day -= 1
    i -= 1

for day in range(1, k + 1):
    if foward[day] == backward[day]:
        print(foward[day] + 1)
