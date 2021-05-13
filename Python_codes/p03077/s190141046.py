import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    people = [int(input()) for _ in range(5)]
    print(math.ceil(n/min(people))+4)
            
if __name__ == '__main__':
    main()