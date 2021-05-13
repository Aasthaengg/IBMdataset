X=int(input())
A=int(input())
B=int(input())

X=X-A

while True:
    X=X-B
    if X-B<0:
        break
    else:
        pass
print(X)