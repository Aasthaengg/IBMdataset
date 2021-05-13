n = input()
cnt = 0
for i in n:
    if i == "7":
        print("Yes")
        break
    else:
       cnt += 1
       if cnt == 3:
           print("No")