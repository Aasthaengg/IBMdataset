week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
s = input()
i = 1
while s != week[-i]:
    i = i + 1
print(int(i))