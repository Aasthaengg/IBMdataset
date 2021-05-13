N = int(input())
A = [int(i) for i in input().split()]
even = sum([1 for a in A if a%2==0])
print(3**N-2**even if even!=0 else 3**N-1)