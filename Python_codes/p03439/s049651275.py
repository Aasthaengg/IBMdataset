import sys
n = int(input())
l = 0
r = n-1
print(0)
sys.stdout.flush()
i = input()
if i == "Vancant": exit()

for _ in range(19):
    m = (l+r)//2
    print(m)
    sys.stdout.flush()
    j = input()
    if j == "Vancant": exit()
    if (m-l)%2 == 0 and i != j: r = m-1
    elif (m-l)%2 == 1 and i == j: r = m-1
    else:
        l = m+1
        i = "Male" if j == "Female" else "Female"