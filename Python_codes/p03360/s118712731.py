number = list(map(int,input().split()))
K = int(input())
number.sort(reverse=True)
print(number[0]*(2**K)+number[1]+number[2])

