N=int(input())
A=list(map(int,input().split()))
sort_A=sorted(A)
max_A=sort_A[-1]
answer=[]
half_A=max_A//2
number=pow(10,9)
answer=0
for n in range(N-1):
    if number>=abs(sort_A[n]-half_A):
        answer=n
        number=abs(sort_A[n]-half_A)
print(max_A,sort_A[answer])
