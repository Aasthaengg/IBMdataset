input()
k = int(input())
(*x,) = map(int, input().split())
print(sum(min(i, abs(k - i)) for i in x) * 2)