N = int(input())
n = len(str(N))
if n <= 2 :
    print(min(N,9))
elif n == 3 :
    print(9+(N-100+1))
elif n == 4 :
    print(9+900)
else :
    print(min(9+900+(N-10000+1),9+900+90000))