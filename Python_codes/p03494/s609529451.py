N = int(input())
A = list(map(int, input().split()))

ans = 100000000000000
for a in A:
    ans = min(ans, (a ^ (a-1)).bit_length())
print(ans-1)
