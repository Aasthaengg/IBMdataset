n = list(input())
flag = False
for i in range(2):
    if n[i] == n[i+1] and n[i+1] == n[i+2]:
        flag = True
if flag:
    print("Yes")
else:
    print("No")