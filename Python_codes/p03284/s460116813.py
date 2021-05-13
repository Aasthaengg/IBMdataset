from sys import  stdin
A, B = [int(x) for x in stdin.readline().rstrip().split()]
if A%B==0:
    print(0)
else:
    print(1)