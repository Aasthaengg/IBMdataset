N, A, B = map(int,input().split())

mini = A + B - N
if mini < 0:
    mini = 0
maxi = min(A,B)
print(maxi,mini)