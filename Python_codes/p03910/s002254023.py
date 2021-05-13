n = int(input())
point = 0
ans = []
for i in range(1, n+1):
    point += i
    ans.append(str(i))
    if point >= n:
        if str(point - n) in ans:
            ans.remove(str(point - n))
        print('\n'.join(ans))
        break