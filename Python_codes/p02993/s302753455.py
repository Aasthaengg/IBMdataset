s = list(input())
for i in range(1, 4):
    if s[i-1] == s[i]:
        print('Bad')
        exit()
print('Good')
