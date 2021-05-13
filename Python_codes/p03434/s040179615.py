N = int(input())
a_s = list(map(int, input().split()))

a_s.sort(reverse=True)
Alice = a_s[0::2]
Bob = a_s[1::2]
print(sum(Alice) - sum(Bob))
