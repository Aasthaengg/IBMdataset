from sys import stdin
n,m,k = [int(x) for x in stdin.readline().rstrip().split()]

for i in range(n+1):
    for j in range(m+1):
        kosuu = (m-j)*i+(n-i)*j
        if kosuu == k:
            print("Yes")
            exit()
print("No")