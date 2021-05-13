N = int(input())
L = [0]*5
for i in range(5):
    L[i]=-(-N//int(input()))
print(max(L)+4)
