s = input()+"2"
k = int(input())

for i,j in enumerate(s):
    if j != "1":
        now = i
        break

if s == "1"*len(s):
    print(1)
else:
    if k-1 < now:
        print(1)
    else:
        print(s[now])