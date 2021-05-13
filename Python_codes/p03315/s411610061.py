t = input()
ans = 0

for i in range(len(t)):
    if t[i] == '+':
        ans += 1 
    elif t[i] == '-':
        ans -= 1 

print(ans)