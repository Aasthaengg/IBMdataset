s=input()
L,R,d=[int(x) for x in s.split()]

seq = list(range(L, R+1))
print(len(list(filter(lambda x: x%d==0,seq))))
