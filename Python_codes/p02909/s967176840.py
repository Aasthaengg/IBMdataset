S = input()


dic = {0:"Sunny",1:"Cloudy",2:"Rainy"}

for a,b in dic.items():
    if b==S:
        index = a


next_ = (index+1)%3
print(dic[next_])