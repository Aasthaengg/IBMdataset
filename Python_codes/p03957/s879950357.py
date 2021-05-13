from sys import stdin

def readString() :
    return  stdin.readline().rstrip()

def solve() :
    S = readString()
    pos = S.find('C')
    if(pos ==-1):
        print("No")
        return
    pos = S[pos:].find('F')
    if(pos !=-1):
        print("Yes")
    else :
        print("No")

solve()