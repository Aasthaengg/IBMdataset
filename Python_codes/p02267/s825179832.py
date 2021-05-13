n = int(input())
s = list(set(map(int, input().split())))
q = int(input())
t = list(map(int, input().split()))
cnt = 0

for i in range(len(s)):
    for j in range(q):
        if s[i] == t[j]:
            cnt += 1

print(cnt)