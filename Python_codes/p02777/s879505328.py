S,T = input().split()
a,b = map(int,input().split())
U = input()

#print(S,T,U)
#print(a,b)

if S == U:
    print(a-1,b)
elif T == U:
    print(a,b-1)
else:
    pass

