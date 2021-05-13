weather = input()

if "R" not in weather:
    print(0)
elif weather.count("R") == 2 and weather[1:2] == "R":
    print(2)
elif weather.count("R") == 3:
    print(3)
else:
    print(1)