import sys, math
line = [s.rstrip("\n") for s in sys.stdin.readlines()][0]
a_point, a_offence, b_point, b_offence = [int(n) for n in line.split(" ")]
j = math.ceil(float(b_point) / a_offence)
k = math.ceil(float(a_point) / b_offence)
if j <= k:
    print("Yes")
else:
    print("No")
