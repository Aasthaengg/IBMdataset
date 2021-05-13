N = int(input())
An = list(map(int, input().split()))
Bn = list(map(int, input().split()))
remain = 0
ans = 0
li = []
for a, b in zip(An, Bn):
    if a >= b:
        li.append(a-b)
    else:
        ans += 1
        remain += (b-a)
if sum(li) < remain:
    ans = -1
elif ans == 0:
    pass
else:
    temp = 0
    for num in sorted(li, reverse=True):
        if temp >= remain:
            break
        temp += num
        ans += 1
print(ans)
