import sys
def LI():
    return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

a,b,x = LI()

print(max(b//x-(a-1)//x,0))