s = list(input())
t = s[0]
for i in range(1, 4):
    if t == s[i]:
        print('Bad')
        exit()
    t = s[i]

print('Good')
