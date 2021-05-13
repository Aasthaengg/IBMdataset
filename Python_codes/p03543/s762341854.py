s=input()
t=[]
for i in range(10):
    t.append(str(i)*3)
for i in t:
    if i in s:
        print("Yes")
        break
else:
    print("No")