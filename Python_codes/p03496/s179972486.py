import math
from collections import deque
def main():
    n = int(input())
    a = [int(t)for t in input().split()]

    if all([a_i>0 for a_i in a]):
        print(n-1)
        for i in range(1,n):
            print(i,i+1)
        
    elif all([a_i<=0 for a_i in a]):
        print(n-1)
        for i in range(1,n)[::-1]:
            print(i+1,i)

    else:
        if abs(min(a))<max(a):
            print(2*n-1)
            pos = a.index(max(a))+1
            for i in range(n):
                print(pos,i+1)
            for i in range(1,n):
                print(i,i+1)


        else:
            print(2*n-1)
            pos = a.index(min(a))+1
            for i in range(n):
                print(pos,i+1)  
            
            for i in range(1,n)[::-1]:
                print(i+1,i)
if __name__ == "__main__":
    main()