c=input()
x="abcdefghijklmnopqrstuvwxyz"
for i in range(25):
    if x[i]==c:
        print(x[i+1])
        break