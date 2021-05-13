import math
A,B,C = map(int, input().split())

#A-B Partern
base1 = A*B
part1_a = math.ceil(C/2)
part1_b = C-part1_a 
ans1 = abs((base1*part1_a)-(base1*part1_b))

#A-C Partern
base2 = A*C
part2_a = math.ceil(B/2)
part2_b = B - part2_a 
ans2 = abs((base2*part2_a)-(base2*part2_b))

#B-C Partern
base3 = B*C
part3_a = math.ceil(A/2)
part3_b = A - part3_a 
ans3 = abs((base3*part3_a)-(base3*part3_b))

print(min(ans1,ans2,ans3))