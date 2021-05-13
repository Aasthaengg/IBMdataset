n = int(input())
a = input().split()

a = list(map(int, a))
a.sort(reverse=True)
alice_n = a[::2]
bob_n = a[1::2]

print(sum(alice_n) - sum(bob_n))