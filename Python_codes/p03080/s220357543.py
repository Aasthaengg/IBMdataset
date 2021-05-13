#エクサウィザーズ 2019 B

num = input("")
RorB = input("")
Rnum = 0

for char in RorB:
    if char == "R":
        Rnum += 1

if int(Rnum) > int(num) - int(Rnum):
    print("Yes")

else:
    print("No")