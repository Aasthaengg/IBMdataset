import sys
input = sys.stdin.readline

def main():
    r,g,b = map(int, input().split())
    k = int(input())
    
    for i in range(k):
        for j in range(k):
            if i+j > k:
                continue
            if r*2**i < g*2**j < b*2**(k-i-j):
                print('Yes')
                return
    print('No')
    
main()