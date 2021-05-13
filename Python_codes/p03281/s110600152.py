n = int(input())
def num_factors(num):
    facts=2
    for i in range(2,num):
        if num%i == 0:
            facts += 1
    return facts

print(sum([num_factors(i)==8 for i in range(1,n+1) if i&1]))