s = input()
s = s[::-1]

num = []
cnt = 0

for i in range(len(s)):
    if s[i] =="W":
        cnt +=1
    else:
        num.append(cnt)
print(sum(num))