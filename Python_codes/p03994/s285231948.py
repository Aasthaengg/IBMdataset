s = input()
k = int(input())

L = []
for i in range(len(s)):
    L.append((ord("z")-ord(s[i])+1))

ans = ""
i = 0
while i < len(s):
    if s[i] == "a":
        ans +="a"
        i +=1
    elif k-L[i] >= 0:
        ans +="a"
        k -=L[i]
        i +=1
    else:
        ans +=s[i]
        i +=1
k = k%26
ans = ans[:-1] + chr(ord(ans[-1]) + k)
print(ans)