S = input()
flag = 0

for i in range(3):
    if S[i] == S[i+1]:
        flag += 1

if flag:
    print('Bad')
else:
    print('Good')
