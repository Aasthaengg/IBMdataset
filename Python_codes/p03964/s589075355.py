N = int(input())
T,A = map(int,input().split())
for i in range(N-1):
    t,a = map(int,input().split())
    T1 = (T+t-1)//t*t
    A1 = (T+t-1)//t*a
    T2 = (A+a-1)//a*t
    A2 = (A+a-1)//a*a
    if A1 < A:
        T,A = T2,A2
    else:
        T,A = T1,A1
print(T+A)
