num = input()
t = 0
for i in range(len(num)-1):
    if num[i] == num[i+1]:
        t = 1
if t == 1:
    print('Bad')
else:
    print('Good')
