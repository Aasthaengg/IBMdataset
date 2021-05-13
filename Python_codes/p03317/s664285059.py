n,k = map(int, input().split()) 
num_list = list(map(int, input().split()))

if (n-k) % (k-1) == 0:
    print((n-k)//(k-1)+1)
else:
    print((n-k)//(k-1) + 2)