n, a, b = map(int, input().split())

# A B -> A
# AB -> B
# AB -> B
# B A -> A
# A  B -> B
# A B  -> A
# A B -> A
#  AB -> B
# A   B -> A
# A  B -> B
# A  B  ->

diff = b - a
if diff % 2 == 0:
    print("Alice")
else:
    print("Borys")
