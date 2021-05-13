n = int(input())
s = [input().split() for _ in range(n)]
for i in range(n):
    s[i].append(i+1)

s = sorted(s,key=lambda x:int(x[1]),reverse=True)
s = sorted(s,key=lambda x:x[0])
for i in range(n):
    print(s[i][2])
