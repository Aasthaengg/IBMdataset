from itertools import permutations
import sys
input = sys.stdin.readline
 

def main():
 
    input = sys.stdin.readline
 
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
 
    L = list(permutations(list(range(1, n + 1))))
    print(abs(L.index(p) - L.index(q)))
 
 
if __name__ == "__main__":
    main()