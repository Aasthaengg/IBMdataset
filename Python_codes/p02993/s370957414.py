s = input()

pre = ""
for x in s:
    if(x==pre):
        print('Bad')
        exit()
    pre = x
print('Good')
