import collections
import itertools


N=int(input())
A=list(map(int,input().split()))
data=collections.Counter(A)

def binbin(a,b,c):
    maxlen=max(len(bin(a)[2:]),len(bin(b)[2:]),len(bin(c)[2:]))
    data2={"x":(maxlen-len(bin(a)[2:]))*"0"+bin(a)[2:],"y":(maxlen-len(bin(b)[2:]))*"0"+bin(b)[2:],"z":(maxlen-len(bin(c)[2:]))*"0"+bin(c)[2:]}

    length=len(data2["x"])
    ite=itertools.permutations("xyz")
    for x,y,z in ite:
        data=[]
        for i in range(length):
            if not (int(data2[x][i]) + int(data2[y][i]))%2 == int(data2[z][i]):
                return(0)
    return(1)


if data[0]==N:
    print("Yes")
elif N%3==0:
    mc=data.most_common()
    if data[0] == N//3 and len(data)==2:
        print("Yes")
    elif len(data)==3 and binbin(mc[0][0],mc[1][0],mc[2][0]) and mc[0][1]==mc[1][1]==mc[2][1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
