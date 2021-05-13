n = int(input())

a = list(map(int,input().split()))

r = [1/i for i in a]

print(1/sum(r))
