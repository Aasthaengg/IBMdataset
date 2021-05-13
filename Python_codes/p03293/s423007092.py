s = input()
t = input()
cnt = 0

for i in range(len(s)):
    if s[-i:]+s[:-i] == t:
        cnt +=1

print("Yes") if cnt > 0 else print("No")