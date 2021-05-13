#template
def inputlist(): return [int(j) for j in input().split()]
#template
suma =0
N = input()
for i in range(len(N)):
    suma+= int(N[i])
if suma % 9 == 0:
    print("Yes")
else :
    print("No")