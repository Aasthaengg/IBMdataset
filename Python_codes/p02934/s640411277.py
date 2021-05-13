n = int(input())
a = list(map(int, input().split()))

a_re = [1/x for x in a]
su_a = sum(a_re)
print(1/su_a)