s = input()
n = len(s)
ans = [1]*n
for i in range(n) :
    if s[i] == "R" and s[i+1] == "R":
        ans[i+2] += ans[i]
        ans[i]=0
    m = n-i-1
    if s[m] == "L" and s[m-1]== "L" :
        ans[m-2] += ans[m]
        ans[m] = 0

print(*ans)



