X,A,B=int(input()),int(input()),int(input())
X-=A
while True:
    if X < B: break
    else: X-=B
print(X)