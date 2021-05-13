n = int(input())
s = input()
t = input()
if s==t:
    print(len(s));exit()

ans = n*2
for i in range(n):
    if s[i:]==t[:n-i]:
        ans = n+i

print(ans)
