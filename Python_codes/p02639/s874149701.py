five = input()
lst_five = five.split(" ")

for i in range(len(lst_five)):
    if lst_five[i] == "0":
        print(i+1)
