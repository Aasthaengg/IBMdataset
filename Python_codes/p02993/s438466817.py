S = input()

res = ''
for s in S:
    if res == s:
        print('Bad')
        exit()
    res = s
print('Good')
