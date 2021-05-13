A, B = map(int, input().split())

sub_AB = abs(A-B)

A_height = 0
for i in range(1, sub_AB):
    A_height += i

print(A_height - A)
