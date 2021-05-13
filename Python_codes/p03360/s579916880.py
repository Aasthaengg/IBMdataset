
abc = list(map(int,input().split()))
k = int(input())
abc.sort()
print(abc[-1]*2**k+abc[0]+abc[1])