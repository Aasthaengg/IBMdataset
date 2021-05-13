input = input()
split = input.split()
H1 = split[0]
M1 = split[1]
H2 = split[2]
M2 = split[3]
K = split[4]
h = int(H2)*60 - int(H1)*60 + int(M2) - int(M1) - int(K)
print(h)