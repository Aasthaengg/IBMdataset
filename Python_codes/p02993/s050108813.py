a = list(input())
flag = 0
for i in range(3):
    if a[i] == a[i+1]:
        flag = 1
if flag == 1:
    print('Bad')
else:
    print('Good')