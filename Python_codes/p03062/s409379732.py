n=int(input())

a= list(map(int,input().split()))

plus = []

minas = []

for value in a:
    if value < 0:
        minas.append(abs(value))
    else:
        plus.append(value)

if len(minas)%2 == 0:
    ans = sum(plus)+sum(minas)
else:
    if len(plus) > 0:
        mini = min(min(plus),min(minas))
        ans = sum(plus)+sum(minas)-mini*2
    else:
        mini = min(minas)
        ans = sum(minas)-mini*2

print(ans)