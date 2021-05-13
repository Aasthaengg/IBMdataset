s = input()
if all(s[i] != s[i+1] for i in range(3)):
    print('Good')
else:
    print('Bad')