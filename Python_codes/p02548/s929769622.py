import sys
input = sys.stdin.readline

def main():
    n = int(input())

    count = [0]*(n)

    for i in range(1, n):
        for j in range(i, n, i):
            count[j] += 1
    
    ans = sum(count)
    print(ans)
    
    
    
    
if __name__ == "__main__":
    main()
