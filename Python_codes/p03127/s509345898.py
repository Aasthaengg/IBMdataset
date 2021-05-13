import math
def main():
    n = (int)(input())
    k = list(map(int,input().split()))
    ans = k[0]
    for i in k:
        ans = math.gcd(ans,i)
    print(ans)

main()