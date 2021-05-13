N = int(input())
S = input()
T = S[:int(N/2)]
O = 'Yes' if N%2==0 and S == T + T else 'No'
print(O)