time, planA, planB = map(int,input().split())

prise_A = time * planA
prise_B = planB

if prise_A >= prise_B:
    print(prise_B)
else:
    print(prise_A)