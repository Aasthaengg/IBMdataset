n = input()
flag = True
for i in range(len(n)//2):
    if n[i] != n[-1*(i+1)]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")