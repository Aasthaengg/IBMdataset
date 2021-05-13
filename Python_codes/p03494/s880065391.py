N = int(input())
A = list(map(int,input().split()))
ans = 0
def GCD(a,b):
    if a < b:
        a,b = b,a
    while a % b != 0:
        a,b = b, a % b
    return b
if __name__ =="__main__":
    for i in range(N-1):
       A[i+1] = GCD(A[i],A[i+1])
    while A[N-1] % 2 == 0:
        A[N-1] //= 2
        ans += 1
    print(ans)