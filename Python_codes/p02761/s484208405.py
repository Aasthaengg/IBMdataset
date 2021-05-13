import sys
n, m = map(int, input().split())

c_dict = {}
flag = False
for _ in range(m):
    s, c = map(int, input().split())
    s -= 1
    if s in c_dict and c != c_dict[s]:
        flag = True
    elif s not in c_dict:
        c_dict[s] = c
if flag:
    print("-1")
    sys.exit()

if 0 in c_dict and c_dict[0] == 0 and n > 1:
    print("-1")
    sys.exit()
ans = ""
for i in range(n):
    if i in c_dict:
        ans += str(c_dict[i])
    elif i > 0:
        ans += "0"
    elif i == 0 and n > 1:
        ans += "1"
    elif i == 0 and n == 1:
        ans += "0"
print(ans)
