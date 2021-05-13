# coding:utf-8
danmen = input()
S1 = []
S2 = []
area = 0 # ?????????????°´???????????¢???

for i, line in enumerate(danmen):
    if line == '\\':
        S1.append(i)
    elif S1 and line == '/':
        loc = S1.pop()
        area += i-loc

        pond_sum = i-loc
        while S2 and S2[-1][0] > loc:
            pond_sum += S2[-1][1]
            S2.pop()

        S2.append([loc,pond_sum])


print(area)
print(len(S2),*(a for j,a in S2))