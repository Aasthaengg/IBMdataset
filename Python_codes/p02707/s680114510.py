n = int(input())
a = input().split()

sub = {}
for i in range(1, n + 1):
    sub[str(i)] = 0

for mng in a:
    sub[mng] += 1

for i in range(1, n + 1):
    print(sub[str(i)])
