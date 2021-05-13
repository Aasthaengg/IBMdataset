from sys import stdin

def main():
    n,k = [int(x) for x in stdin.readline().rstrip().split()]
    ans = n - k + 1
    print(ans)
    
if __name__=='__main__':
    main()