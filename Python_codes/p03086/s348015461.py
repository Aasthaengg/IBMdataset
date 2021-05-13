S = list(input())

count = 0
maximam = 0
for i in S:
    if i == 'A' or i == 'C' or i == 'G' or i == 'T':
        count += 1
    else :
        count = 0
    if count > maximam:
        maximam = count
print(maximam)