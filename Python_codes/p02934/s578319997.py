N=int(input())
number=list(map(int,input().split()))
number_reverse=[1/i for i in number]
print(1/sum(number_reverse))
