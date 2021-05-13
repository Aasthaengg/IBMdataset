import sys
def LS2(): 
    return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()

print(s[0]+str(len(s)-2)+s[-1])