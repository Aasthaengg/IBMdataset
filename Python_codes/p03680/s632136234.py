N = int(input())
ls = []
ans = -1
for i in range(N):
    ls.append(int(input()))
on = 0
for i in range(N):
    on = ls[on]-1
    if on == 1:
        ans = i +1
        break
print(ans)