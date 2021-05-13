from bisect import bisect_left,bisect_right
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
#print(A)
#print(B)
#print(C)
for b in B:
    num1 = bisect_left(A,b)
    num2 = bisect_right(C,b)
    #print(num1,b,num2)
    ans += num1*(n-num2)

print(ans)
