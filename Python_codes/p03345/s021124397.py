A,B,C,k = map(int,input().split())
s1 = A-B
s2 = B-A
if k%2 == 0:
    print(s1)
elif k%2 == 1:
    print(s2)
