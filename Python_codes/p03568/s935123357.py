N = int(input())
even = sum([1 for i in input().split() if int(i)%2==0])
print(3**N-2**even if even!=0 else 3**N-1)