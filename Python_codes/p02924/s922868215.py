N = int(input())
if N == 1:
    print(0)
elif N%2 != 0:
    print((1+(N-1))*((N-1)//2))
else:
    print((1+(N-1))*((N-1)//2)+(N-1)//2+1)