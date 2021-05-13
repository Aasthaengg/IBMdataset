n = int(input())
lst1 = [list(input().split()) for i in range(n)]
x = input()

for i in range(n):
    if x == lst1[i][0]:
        theindex = i
        break
ans = 0
for i in range(theindex+1,n):
    ans += int(lst1[i][1])

print(ans)