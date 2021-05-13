s = input()
N = len(s)
dic = {}
for i in range(N):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1

ans = 100
for key in dic:
    temp = list(s)
    cnt = 0
    while temp.count(temp[0]) < len(temp):
        new = [0]*(len(temp)-1)
        for i in range(len(temp)-1):
            if temp[i] == key or temp[i+1] == key:
                new[i] = key
            else:
                new[i] = temp[i]
        cnt += 1
        temp = new
    ans = min(ans, cnt)
print(ans)