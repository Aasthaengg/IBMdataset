s = str(input())

if len(s)%2:
    print('No')
    exit()
for i in range(len(s)):
    if not i%2 and s[i] == "h":
        continue
    elif i%2 and s[i] == "i":
        continue
    else:
        print("No")
        exit()
print('Yes')