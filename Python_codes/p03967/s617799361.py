s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == "g":
        cnt+=1
    else:
        cnt-=1

print(cnt//2)
