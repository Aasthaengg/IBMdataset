A,B,C= list(map(int, input().strip().split()))
a=A%B
f="NO"
for i in range(B):
    if (a*i)%B==C:
        f="YES"
        break
print(f)
