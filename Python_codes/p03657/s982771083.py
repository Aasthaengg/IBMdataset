A,B = map(int,input().split())
a=A+B
l = [A,B,a]
for i in range(3):
    if l[i]%3==0:
        print("Possible")
        exit()

print("Impossible")