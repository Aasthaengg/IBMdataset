# ABC053
S = input()
a_index = 10**10
z_index = -1
for i in range(len(S)):
    if S[i] == "A":
        a_index = min(a_index, i)
    if S[i] == "Z":
        z_index = max(z_index, i)
print(z_index-a_index+1)