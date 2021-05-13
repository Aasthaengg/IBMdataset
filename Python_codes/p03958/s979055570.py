import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
    
k, t = invr()
ips = sorted(list(invr()))
rest_sum = sum(ips[:-1])
if rest_sum > ips[-1]:
    print(0)
else :
    print(ips[-1]-rest_sum-1)
