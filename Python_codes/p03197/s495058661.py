N=int(input())
A=[int(input())for _ in range(N)]
print('sfeicrosntd'[any(a%2 for a in A)::2])