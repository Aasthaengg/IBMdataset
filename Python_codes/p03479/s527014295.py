from sys import stdin

[X, Y] = [int(x) for x in stdin.readline().rstrip().split()]

index=1
while(True):
    X = 2*X
    if X<=Y:
        index+=1
    else:
        break

print(index)
    



