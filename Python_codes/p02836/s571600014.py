#<B>
s = input()
a = s[:len(s)//2]
a = a[::-1]
if len(s) % 2 == 0:
    b = s[len(s) // 2:]
else:
    b = s[len(s) // 2 + 1:]

ans = 0
for (x, y) in zip(a, b):
    if x != y:
        ans += 1
print(ans)
        
