n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

s_l = list(set(s))
cnt = []

for i in s_l:
    cnt.append(s.count(i)-t.count(i))
    
if max(cnt) <= 0:
    print(0)
else:
    print(max(cnt))