N = int(input())
j = 0
z = 0
r = 'No'
for i in range(N):
    n, m = map(int, input().split())
    if n == m:
        j += 1
    else:
        j = 0
    if j == 3:
        r = 'Yes'
        break
print(r)