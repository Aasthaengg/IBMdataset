# B.py

S = str(input())
a_point = []
z_point = []

for i in range(len(S)):
    if S[i] == "A":
        a_point.append(i)
    if S[i] == "Z":
        z_point.append(i)

print(max(z_point)-min(a_point)+1)
