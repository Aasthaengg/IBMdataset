N, M = [int(i) for i in input().split()]    
print(M//2 if M <= 2*N else N+(M-2*N)//4)