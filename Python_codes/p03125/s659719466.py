B,A=list(map(int,input().split()))

which=A%B

if which==0:
    print(A+B)
else:
    print(A-B)