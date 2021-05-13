temp = input()
temp2 = temp.split(" ")
temp = []
for i in temp2:
    temp.append(int(i))

for i in range(1,100000000):
    ans1 = temp[0]*i
    if ans1 % temp[1] != 0:
        break
    if ans1 >= 10^18:
        ans1 = -1
        break
print(ans1)