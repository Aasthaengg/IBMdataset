c_1 = list(map(int, input().split()))
c_2 = list(map(int, input().split()))
c_3 = list(map(int, input().split()))

diff = []

for i in range(2):
    diff.append(c_1[i] - c_1[i+1])

if c_2[0] - c_2[1] != diff[0] or c_2[1] - c_2[2] != diff[1]:
    print("No")
    exit()

if c_3[0] - c_3[1] != diff[0] or c_3[1] - c_3[2] != diff[1]:
    print("No")
    exit()

print("Yes")
