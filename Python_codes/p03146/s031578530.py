def collatz(n):
    return 3*n+1 if n%2 else n//2
a,n=[],int(input())
while len(set(a))==len(a):
    a.append(n)
    n=collatz(n)
print(len(a))