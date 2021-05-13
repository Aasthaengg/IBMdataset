N = input()
for i in range(10):
    if N.count(str(i)*3)or N.count(str(i)*2)or N.count(str(i)*4):
        print('Bad')
        exit()
print('Good')

