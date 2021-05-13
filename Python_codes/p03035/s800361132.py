age,fee=map(int,input().split())

if age>=13:
    print(fee)
elif age<13 and age>=6:
    print(int(fee/2))
else:
    print(0)
