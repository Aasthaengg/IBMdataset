import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a = int(input())
    exist = [0] * (10**6 + 1)
    exist[a] = 1
    ans = 1
    while(True):
        ans += 1
        if a%2 == 0: 
            a //= 2
        else: 
            a = 3*a + 1
        if exist[a] == 1: 
            print(ans)
            return
        else: 
            exist[a] = 1
        
if __name__ == '__main__':
    main()