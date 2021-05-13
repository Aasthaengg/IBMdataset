N = int(input())
S = input()
print('Yes' if(S[:int(N/2)] == S[int(N/2):]) else 'No')
