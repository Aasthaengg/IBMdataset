coffee = input()

if len(coffee) != 6:
    print("文字数が異なります")

if coffee[2] == coffee[3] and coffee[4] == coffee[5]:
    print("Yes")
else:
    print("No")