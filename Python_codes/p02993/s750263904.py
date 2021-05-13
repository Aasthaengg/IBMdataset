a = input()

flag = True

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        flag = False
        break

if flag:
    print("Good")
else:
    print("Bad")