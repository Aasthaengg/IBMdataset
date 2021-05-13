import copy
import math


def main():
    n=int(input())
    temp=input().split(" ")
    nums=list(map(int,temp))
    nums.reverse()
    l=2 # min 
    r=2 # max
    for num in nums:
       # if num<=l and num>=r:
        r=(int(r/num)+1)*(num)-1
        l= math.ceil(l/num)*num
        
        if l>r:
             print("-1")
             return 0
    print(str(l)+" "+str(r))      
    



if __name__ == '__main__':
    main()
