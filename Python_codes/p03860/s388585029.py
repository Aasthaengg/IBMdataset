import sys
def LS2(): 
    return list(sys.stdin.readline().rstrip())  #空白なし

print('A'+LS2()[8]+'C')