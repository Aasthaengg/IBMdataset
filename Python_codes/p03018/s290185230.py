s = str(input())
lis = []
cnt = 0

while cnt < len(s):
    if cnt+1 < len(s) and (s[cnt] == "B" and s[cnt+1] == "C"):
        lis.append("D")
        cnt += 1
    else:
        lis.append(s[cnt])
    cnt += 1
  #    print(lis)

ans = 0
num = 0
for i in range(len(lis)):
    if lis[i] == "A":
        num += 1
    elif lis[i] == "D":
        ans += num
    else:
        num = 0
print(ans)