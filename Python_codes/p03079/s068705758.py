temp = input()
temp_spl = temp.split()
a = int(temp_spl[0])
b = int(temp_spl[1])
c = int(temp_spl[2])

if a == b and b == c and b >=1 and b <= 100:
    print("Yes")
else:
    print("No")