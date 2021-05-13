n = input()
s = list(map(int,input().split()))
c = 0
for i in s:
    if i % 2 == 1:
        c+=1
if c % 2 == 1:
    print("NO")
else:
    print("YES")