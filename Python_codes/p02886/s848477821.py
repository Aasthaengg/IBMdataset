N = int(input())
d = [int(x) for x in input().split()]
print((pow(sum(d),2)-sum([pow(x,2) for x in d]))//2)