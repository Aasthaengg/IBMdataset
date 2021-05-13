N = int(input())
for i in range(int(N**(1/2)),0,-1):
    if N%i == 0:
        a = N // i
        b = i
        break
print(a+b-2)