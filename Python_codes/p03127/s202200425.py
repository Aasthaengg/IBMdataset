import fractions
N=int(input())
a=input().split()
A=[int(b) for b in a]
A=sorted(A,reverse=True)
numbers=[]
numbers.append(fractions.gcd(A[0],A[1]))
for a in range(1,N):
    answer=fractions.gcd(numbers[-1],A[a])
    numbers.append(answer)
print(numbers[-1])
