n = int(input())
s = input()

ls = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2

ans = ''
for c in s:
    ans += ls[ls.index(c) + n]
print(ans)