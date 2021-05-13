a = []
while True:
    b = input()
    b = int(b)
    if b == 0:
        break
    else:
        a.append(b)
for i in range(len(a)):
    c = i+1
    print("Case "+str(c)+": "+str(a[i]))
