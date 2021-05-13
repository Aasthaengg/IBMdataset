s = input()
w = int(input())
ans = ""
i = 0
while i*w<len(s):
    ans +=s[i*w]
    i += 1
    if i*w >=len(s):
        break
print(ans)