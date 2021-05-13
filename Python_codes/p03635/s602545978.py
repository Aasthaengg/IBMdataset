import sys
def LI(): 
    return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

n,m = LI()

print((n-1)*(m-1))