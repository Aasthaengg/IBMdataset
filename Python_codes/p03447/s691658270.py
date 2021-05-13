X,A,B=[int(input()) for _ in range(3)]
XX=X-A

Ans=[XX-s*B for s in range((XX//B)+1)]
print(Ans[-1])