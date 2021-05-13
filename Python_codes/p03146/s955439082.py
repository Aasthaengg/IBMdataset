s = int(input())

a = [s]
for i in range(10**6):
    if a[i]%2 == 0:
        ai = a[i]// 2
    else:
        ai = 3*a[i]+1
    if ai in a:
        ans = i + 2
        break
    a.append(ai)
print(ans)