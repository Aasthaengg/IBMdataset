import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,K = map(int,input().split())
    a = np.array(list(map(int,input().split())))
    s = sum(a)
            
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        return divisors
            
    div = make_divisors(s)
    
    div.sort()
    ans = 1
    for use in div:
        rest = -(a%use)
        rest = np.sort(rest)
        ch = -sum(rest)//use
        do = use*ch+sum(rest[:ch])
        if do <= K:
            ans = use
    
    print(ans)

if __name__ == "__main__":
    main()
