t = input()

ans = ""

for i in range(len(t)):
    if t[i] == '1':
        ans+='9'
    elif t[i] == '9':
        ans+='1'

print(ans)