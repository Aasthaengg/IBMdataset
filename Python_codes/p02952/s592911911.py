N = int(input())
print(sum(len(str(n))%2==1 for n in range(1,1+N)))