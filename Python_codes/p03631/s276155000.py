A=int(input())
B=int(A/100)+(A%10)*100+(int(A/10)%10)*10
if A==B:
    print('Yes')
else:
    print('No')