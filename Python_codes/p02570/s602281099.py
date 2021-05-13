import math
def digit():
    return int(input())
def list1():
    return list(map(int,input().split()))
def isperfectsquare(n):
    return True if int(math.sqrt(n)+0.5)**2==n else False

def main():
    s,t,d=list1()
    print('Yes' if s/d<=t else 'No')
main()
