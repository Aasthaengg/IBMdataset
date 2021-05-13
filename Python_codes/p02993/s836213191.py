s = input()
print('Bad' if sum(s[i] == s[i + 1] for i in range(3)) else 'Good')