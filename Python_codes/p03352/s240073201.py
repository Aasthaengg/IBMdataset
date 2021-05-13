X = int(input())
check =[]
check2=[]
for i in range(1,33):
    for s in range(2,11):
        check.append(pow(i,s))

#print(check)
for i in check:
    if i<=X:
        check2.append(i)
print(max(check2))
