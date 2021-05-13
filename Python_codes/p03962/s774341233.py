penki = [i for i in map(int, input().split())]
count = 3
if penki[0] == penki[1]:
    count -= 1
if penki[0] == penki[2]:
    count -= 1
if penki[1] == penki[2]:
    count -= 1
if penki[1] == penki[2] == penki[0]:
    count += 1
print(count)