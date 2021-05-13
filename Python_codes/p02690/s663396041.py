X =int(input())
def jug(n):
    if n>0:
        return 1
    else:
        return -1

ALL = [i**5 for i in range(-200,200+1)]
for a in ALL:
    for b in ALL:
        if a-b ==X:
            ans =[jug(a)*int(abs(a)**(1.0/5)),jug(b)*int(abs(b)**(0.2))]
            print(ans[0],ans[1])
            exit()