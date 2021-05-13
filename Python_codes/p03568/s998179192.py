N = int(input())
A = list(map(int,input().split()))
even = [i for i in A if i%2==0]
# print(even)
ans = 3**N - 2**(len(even))
print(ans)