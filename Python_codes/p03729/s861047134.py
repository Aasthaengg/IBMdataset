a = input()
list_a = a.split(" ")
b = [] #リスト作成
for i in range(len(list_a)):
    b.append(list(list_a[i]))
if b[0][-1] == b[1][0] and b[1][-1] == b[2][0]:
    print("YES")
else:
    print("NO")