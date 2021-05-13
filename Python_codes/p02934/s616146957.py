N = int(input())
A = map(int, input().split())
sum = sum(1/a for a in A)
print(1/sum)