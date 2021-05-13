N = int(input())
S = input() 
a=int(N/2)
print('Yes' if N%2==0 and S[:a]==S[a:] else 'No')