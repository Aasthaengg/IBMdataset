#-------------
N = int(input())
#-------------
cnt = 0
while True:
    X = 2**cnt
    if N//2 >= X:
        cnt +=1
    else:
        break
print(X)