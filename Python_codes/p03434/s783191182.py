N=int(input())
a = list(map(int, input().split()))
b=sorted(a, reverse=True)
print(sum(b[0::2])-sum(b[1::2]))