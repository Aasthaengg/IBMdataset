s = str(input())

cnt = 0
for i in range(1,len(s)-1):
    cnt += 1

print(s[0]+str(cnt)+s[len(s)-1])