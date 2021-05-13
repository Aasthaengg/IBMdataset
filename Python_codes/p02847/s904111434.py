a = input()
my_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
if a == "SUN":
    print(7)
for i in range(0, (len(my_list)-1)):
    if a == my_list[i]:
        print(6-i)