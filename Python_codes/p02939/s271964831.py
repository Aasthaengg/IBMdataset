S = input()
a = ''
b = ''
ans = 0

for i in S:
    a += i 
    if a != b:
        ans += 1
        b = a 
        a = ''
print(ans)
