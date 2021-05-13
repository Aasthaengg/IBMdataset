def lo2(n):
    count = 0
    while n%2==0:
        n=n//2
        count+=1
    return count

N = int(input())
A = list(map(int,input().split()))
A = list(map(lo2,A))
print(min(A))
