N = int(input())
a = list(map(int, input().split()))
a_rev = sorted(a)[::-1]
a_rev = a_rev[1::2]
print(sum(a_rev[:N]))