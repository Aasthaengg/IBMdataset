N = input()
count = 0
tmp = 'null'
ans = 'No'

for n in N:
    if tmp == n:
        count += 1
        if count == 2:
            ans = 'Yes'
            break
    else:
        count = 0
        tmp = n

print(ans)