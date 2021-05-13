n = int(input())
*a, = map(int, input().split())
odd = 2**sum(i%2==0 for i in a)
print(3**n - odd)