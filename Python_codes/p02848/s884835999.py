n = int(input())
s = input()
 
def ROTN(tmp, n):
    tmp = ord(tmp) + n
    if tmp > 0x5a:
        tmp -= 26
    return chr(tmp)
 
 
ans = []
for i in range(len(s)):
    tmp = s[i]
    ans.append(ROTN(tmp, n))
 
for i in range(len(ans)):
    print(ans[i], end="")