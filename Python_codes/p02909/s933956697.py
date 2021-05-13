# 141 A

prompt = input()
l = ["Sunny", "Cloudy", "Rainy"]

for i in range(3):
    if prompt == l[i]:
        try:
            print(l[i+1])
        except:
            print(l[(i+1)-len(l)])