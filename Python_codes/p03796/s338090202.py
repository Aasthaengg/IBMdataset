N = int(input())
fact = 1
for integer in range(1,N+1):
    fact = fact * integer % 1000000007
print(fact)