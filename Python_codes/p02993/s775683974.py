n = input()

for i in range(3):
    if n[i] == n[i+1]:
        print('Bad')
        break

else:
    print('Good')
