import sys
import math

def main():

    input = sys.stdin.readline

    a,b = map(int, input().split())
    a_total = 1 
    ans = 0
    while (a_total < b):
        a_total += a-1
        ans +=1
    print(ans)
    

if __name__ == "__main__":
    main()