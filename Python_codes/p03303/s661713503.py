s = input()
n = int(input())
ans = ''
m = 0
while m < len(s):
    ans += s[m]
    m += n
    
print(ans)