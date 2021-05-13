n = int(input())
s = input()

lst = []
for i in range(1,n-1):
    left = s[:i]
    right = s[i:]

    cnt = 0
    for j in set(left):
        if j in set(right):
            cnt += 1
    lst.append(cnt)

if not lst:
    print(0)
else:
    print(max(lst))