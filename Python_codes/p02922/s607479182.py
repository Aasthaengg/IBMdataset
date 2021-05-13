A,B=map(int,input().split())
s=A
if B==1:
    print(0)
    exit()
for i in range(1,100):
    if s>=B:
        break
    s+=A-1
print(i)