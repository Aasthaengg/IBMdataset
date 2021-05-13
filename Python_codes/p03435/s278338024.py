G1 = list(map(int, input().split()))
G2 = list(map(int, input().split()))
G3 = list(map(int, input().split()))
sub_G1 = []
sub_G2 = []
sub_G3 = []
sub_R12 = []
sub_R23 = []
for i in range(2):
  sub_G1.append(G1[i+1] - G1[i])
  sub_G2.append(G2[i+1] - G2[i])
  sub_G3.append(G3[i+1] - G3[i])
for k in range(3):
  sub_R12.append(G2[i]-G1[i])
  sub_R23.append(G3[i]-G2[i])
condition1 = bool(sub_G1[0] == sub_G2[0] == sub_G3[0])
condition2 = bool(sub_G1[1] == sub_G2[1] == sub_G3[1])
condition3 = bool(len(set(sub_R12)) == 1)
condition4 = bool(len(set(sub_R23)) == 1)
if condition1 and condition2 and condition3 and condition4:
  print("Yes")
else:
  print("No")