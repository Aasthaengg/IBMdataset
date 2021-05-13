alp = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
keta = 0
a = 0
answer = ''
while a < n:
    keta += 1
    a += 26**keta
a -= 26**keta
n -= a+1
for i in range(keta-1):
    answer += alp[n // (26 ** (keta-i-1))]
    n = n % (26 ** (keta-i-1))
answer += alp[n % 26]
print(answer)