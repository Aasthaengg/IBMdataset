n = int(input())
print(sum([n//i-1 for i in range(1, int(n**(1/2))+1) if (n%i==0) and (n//i-1 > i)]))