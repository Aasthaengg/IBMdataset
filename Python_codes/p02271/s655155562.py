n = int(input())
SET1 = {0}
for a in map(int, input().split()):
    for b in tuple(SET1):
        SET1.add(a + b)
input()
for m in map(int, input().split()):
    print('yes' if m in SET1 else 'no')
