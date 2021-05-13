S = str(input())
ls = len(S)
odd_list = []
result = ""

while ls > 0:
    ls -= 1
    if ls % 2 == 0:
        odd_list.append(ls)
odd_list = sorted(odd_list)
# print(odd_list)

for i in odd_list:
    result = result + S[i]
print(result)