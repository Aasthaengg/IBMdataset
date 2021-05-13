n = int(input())
s = input()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

for i in s:
    ans += abc[(abc.index(i) + n )% 26]
    
print(ans)