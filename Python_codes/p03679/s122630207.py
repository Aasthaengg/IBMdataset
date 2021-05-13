tmp = input().split(" ")
X = int(tmp[0])
A = int(tmp[1])
B = int(tmp[2])
 
print("delicious") if B <= A else print("safe") if B <= A + X else print("dangerous")