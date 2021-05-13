A,B = map(int,input().split())
ii = 0
for i in range(A,B+1):
    Is = str(i)
    if Is[0] == Is[4] and Is[1] == Is[3]:
        ii += 1
print(ii)