def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    s1 = 0
    for i in range(1,n,2):
        s1 += a[i]
    x1 = s-2*(s1)
    ans = [x1]
    for i in range(n-1):
        ans.append(2*a[i]-ans[-1])
    print(*ans)
    
main()