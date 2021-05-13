n = int(input())
s = input()

countR = 0
for i in range(n):
    if s[i] == "R":
        countR += 1

if countR > n / 2:
    print("Yes")
else:
    print("No")
               
        


    







        

