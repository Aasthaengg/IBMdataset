N = int(input())
A = list(map(int, input().split()))

li = []

for i in range(N-1):
    if A[i+1] - A[i] > 0:
       li.append('+')
    elif A[i+1] - A[i] < 0:
        li.append('-')
    else:
        pass
# print(li)
ans = 1
p = 0
m = 0
for i in li:
    if i == '+':
        p = 1
    elif i == '-':
        m = 1
    if p == 1 & m == 1:
        ans += 1
        p = 0
        m = 0
print(ans)