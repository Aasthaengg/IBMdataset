x = input()
for i in range(1,len(x)):
    if x[i-1] == x[i]:
        print("Bad")
        break
    if i == len(x)-1:
        print("Good")
        break