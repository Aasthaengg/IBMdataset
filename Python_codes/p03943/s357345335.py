import sys

def main(a,b,c):
    if (a+b-c)*(b+c-a)*(c+a-b)==0:
        return 'Yes'
    else:
        return 'No'

a,b,c=map(int,sys.stdin.readline().strip().split())
print(main(a,b,c))
