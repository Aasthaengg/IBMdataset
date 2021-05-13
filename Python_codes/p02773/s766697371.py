#listの要素をキー、その出現数を値として持つディクショナリを返す
def count(list):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = dict.get(list[i], 0) + 1
    return dict

n = int(input())
s = []
for _ in range(n):
    s.append(input())

dic = count(s)
lst = sorted(dic.items(), key=lambda x: x[1], reverse=True)
value_max = lst[0][1]
output = []

for name in lst:
    if name[1] == value_max:
        output.append(name[0])
    else:
        break

output.sort()
print(*output,sep="\n")