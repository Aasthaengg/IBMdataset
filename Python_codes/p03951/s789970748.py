n = int(input())
s = input()
t = input()

ans=n*2
for i in range(n,-1,-1):
    if s[n-i:]==t[:i]:
        ans=n*2-i
        break
print(ans)