s = input()

a = 'ans = 0'

for i in range(4):
   a += s[i] + '1'

exec(a)

print(ans)