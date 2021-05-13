n=int(input())

memo = 0

if n == 1 or n ==2:
    print(n)
    exit()


for i in range(1,n):
    memo += i
    if n <= memo:
        check = i
        break

ans = []

for i in range(check,0,-1):
    n -= i
    #print(i,n)
    ans.append(i)
    if n < i:
        ans.append(n)
        break
ans.sort()

for i in ans:
    print(i)