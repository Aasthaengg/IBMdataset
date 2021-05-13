N=input()
number=0
for a in N:
    if int(a)==9:
        print('Yes')
        break
    else:
        number+=1
if number==2:
    print('No')
