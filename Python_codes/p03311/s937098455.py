N=int(input())
B=sorted(int(x)-i-1 for i,x in enumerate(input().split()))
def sad(x):
    return sum(abs(b-x)for b in B)
print(sad(B[N//2]))
