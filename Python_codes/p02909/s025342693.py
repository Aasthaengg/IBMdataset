n = input()
my_list = ["Sunny", "Cloudy", "Rainy", "Sunny"]
a = ""
for i in range(0, len(my_list)):
    if n==my_list[i]:
        a += my_list[i+1]
        break
print(a)