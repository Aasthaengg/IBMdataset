n = int(input())
num = 0
ans = []
for i in range(1,10001):
    num += i
    ans.append(i)
    if num >= n:
        break
if num != n:
    ans.remove(num - n)
for i in ans:
    print(i)