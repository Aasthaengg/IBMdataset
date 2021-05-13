import sys
 
def eat(i,j,candies,counter):
    s=candies[i]+candies[j]
    if s>x:
        if candies[i]>=s-x:
            candies[i]-=s-x
        else:
            candies[j]-=s-x-candies[i]
            candies[i]=0
        counter+=s-x
    return counter
 
def main(n,x,candies):
    counter=0
    for i in range(1,n):
        counter=eat(i,i-1,candies,counter)
    return counter
 
n,x=map(int,sys.stdin.readline().strip().split())
candies=list(map(int,sys.stdin.readline().strip().split()))
print(main(n,x,candies))