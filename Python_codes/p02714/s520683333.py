import sys
input = sys.stdin.readline
def main():
    n= int(input())
    s = str(input().rstrip())
    r= s.count('R')
    g=s.count('G')
    b = s.count('B')
    ans = 0
    for i in range(n-2):
        for j in range(i+1, (n+i+1)//2):
            k = 2*j-i
            t = {s[i], s[j], s[k]}
            if len(t) ==3:
                ans +=1
    print(r*g*b-ans)
if __name__ == '__main__':
    main()