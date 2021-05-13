X=int(input())
A=int(input())
B=int(input())

money=X
money -= A
money -= B*(money//B)

print(money)