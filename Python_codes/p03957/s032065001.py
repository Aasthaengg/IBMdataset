s = input()
now = ["C","F"]
now_k = 0
flag = 0
for i in range(len(s)):
    if s[i] == now[now_k]:
        now_k += 1
        if now_k == 2:
            print("Yes")
            flag = 1
            break
if flag == 0:
    print("No")