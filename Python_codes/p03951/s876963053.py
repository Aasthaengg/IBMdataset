n = int(input())
s = input()
t = input()
ans = 0
for i in range(n):
    dum1 = s[n-i-1:n]
    dum2 = t[0:i+1]
    if dum1 == dum2:
        ans = n*2-((i+1))
if ans == 0:
    ans = n*2
print(ans)