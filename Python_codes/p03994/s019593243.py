s = input()
K = int(input())
k = K

ans = ""
for i in range(len(s)-1):
    if(s[i] == "a"):
        ans += s[i]
        continue
    if(ord(s[i])+k >= ord("z")+1):
        ans += "a"
        k -= ord("z")+1-ord(s[i])
    else:
        ans += s[i]

a = ord(s[-1])+k%26
if(a > ord("z")):
    a -= 26
ans += chr(a)
    
print(ans)