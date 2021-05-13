N = int(input().strip())
A = list(map(int, input().strip().split(' ')))

c_even = len([1 for a in A if a % 2 == 0])
ans = 3**len(A) - 2**c_even
print(ans)
