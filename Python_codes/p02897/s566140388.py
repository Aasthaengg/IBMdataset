N = int(input())
if N%2 == 0:
    print(1/2)
else:
    tmp = ((N-1)/2) + 1
    print(tmp/N)
