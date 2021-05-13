N = int(input())
a = [int(input())-1 for _ in range(N)]

i = 0
c = 0
flag = 0
for _ in range(N):
    i = a[i]
    c += 1
    if i == 1:
        flag = 1 
        break

ans = c if flag else -1
print(ans)