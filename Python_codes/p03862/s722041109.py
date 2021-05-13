import sys

def eat(i,candies,counter):
    s=candies[i]+candies[i-1]
    nc=max(0,s-x)
    counter+=nc
    candies[i]-=nc
    return counter

def main(n,x,candies):
    counter=0
    if candies[0]>x:
        counter=candies[0]-x
        candies[0]=x
    for i in range(1,n):
        counter=eat(i,candies,counter)
    return counter

n,x=map(int,sys.stdin.readline().strip().split())
candies=list(map(int,sys.stdin.readline().strip().split()))
print(main(n,x,candies))
