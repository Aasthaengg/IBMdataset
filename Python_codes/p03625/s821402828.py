n = int(input())
a_list = sorted([int(x) for x in input().split()], reverse=True)
ans = 0
temp = 0
count = 0
e = None
for i in range(n):
    if a_list[i] == temp:
        count += 1
        if count == 2:
            if e is None:
                e = temp
                count -= 2
            else:
                ans = e * temp
                break
    else:
        temp = a_list[i]
        count = 1
print(ans)