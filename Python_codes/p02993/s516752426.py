number = input()
check = False
for i in range(len(number)-1):
    if number[i] == number[i+1]:
        check = True
if check == True:
    print("Bad")
else:
    print("Good")
