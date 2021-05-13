def LucasNumber(N):
    if N==0:
        return 2
    elif N==1:
        return 1
    else:
        Li2 = 2
        Li1 = 1
        for T in range(2,N+1):
            Li0 = Li1+Li2
            Li2 = Li1
            Li1 = Li0
        return Li0
      
print(LucasNumber(int(input())))