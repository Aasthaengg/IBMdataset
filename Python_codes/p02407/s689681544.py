input()
x=[int(i) for i in input().split()]
for i in x[::-1]:
    if i==x[0]:
        print(i)
    else:
        print(i,end=" ")