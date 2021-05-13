n = int(input())
s = input()
t = input() + 'x'

for i in range(n):
    if s[i:]==t[:~i]:
        print(n+i)
        exit()

print(2*n)
