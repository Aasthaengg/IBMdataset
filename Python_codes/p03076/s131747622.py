import math

lst = []
min_1 = "129"
for i in range(5):
    s = input()
    lst.append(s)
    if s[-1] != "0" and s[-1] <= min_1[-1]:
        min_1 = s
if min_1 == "129": min_1 = lst[0]        
lst.remove(min_1)
a = list(map(lambda x:math.ceil(int(x)/10)*10,lst))
print(sum(a) + int(min_1))