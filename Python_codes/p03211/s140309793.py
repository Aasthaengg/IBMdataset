S = input()
list =[]

for i in range(len(S)-2):
    list.append(int(S[i]+S[i+1]+S[i+2]))

min_sa = 1000
for i in list:
    sa = abs(753-i)
    min_sa = min(sa,min_sa)

print(min_sa)