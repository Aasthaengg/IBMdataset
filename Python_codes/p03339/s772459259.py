n = int(input())
s = input()
west = []
east = []
count_w = 0
count_e = 0

for i in s:
    if i == "W":
        count_w+=1
    west.append(count_w)
for j in reversed(s):
    if j == "E":
        count_e +=1
    east.append(count_e)
r_east = [k for k in reversed(east)]
   
attention = [west[i] + r_east[i] for i in range(n)]
print(min(attention)-1)