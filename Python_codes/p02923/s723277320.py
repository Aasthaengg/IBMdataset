n = input()
b = list(map(int,input().split(' ')))
ans = 0
lst = []
for i in range(int(n)-1) :
    if b[i] >= b[i+1]:
        ans += 1
    else:
        lst.append(ans)
        ans = 0
lst.append(ans)
print(max(lst))
