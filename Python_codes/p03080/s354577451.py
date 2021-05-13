n=int(input())
s=input()
x,y=s.count('R'),s.count('B')
if(x>y):
    print("Yes")
else:
    print("No")