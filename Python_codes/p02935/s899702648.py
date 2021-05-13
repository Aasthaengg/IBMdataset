N = int(input())
M = list(map(int,input().split()))

M.sort()
x = (M[0]+M[1])/2

for m in M[2:] :
    x = (x+m)/2

print(x)