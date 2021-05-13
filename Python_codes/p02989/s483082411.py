n = int(input())
d = sorted(list(map(int,input().split())))
x = int(n/2)
abc = d[:x]
arc = d[x:]
cnt = 0
for i in range(max(abc)+1, min(arc)+1):
    cnt += 1

print(cnt)