N = int(input())
hon_list = ["pon","pon","hon","bon","hon","hon","pon","hon","pon","hon",]
hon_dict = {}
for i in range(10):
    hon_dict[i] = hon_list[i]

print(hon_dict[N % 10])