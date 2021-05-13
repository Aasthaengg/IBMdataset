N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

mass_prepare = []
change_count = 0
total_minus = 0
for i in range(N):
    diff = A[i] - B[i]
    if diff < 0:
        change_count += 1
        total_minus += diff
    elif diff > 0:
        mass_prepare.append(diff)
mass_prepare.sort()
mass_prepare.reverse()
total = 0
for i in range(len(mass_prepare)+1):
    if total >= abs(total_minus):
        print(i+change_count)
        break
    if i == len(mass_prepare):
        print(-1)
        break
    total += mass_prepare[i]
