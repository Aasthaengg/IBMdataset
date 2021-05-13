N = int(input())

s = ""
for i in range(12):
    if 26*(26**i-1)/25 < N and N <= 26*(26**(i+1)-1)/25:
        t = i#桁数-1
        break

#print(t + 1)
N = int(N - 26*(26**t-1)/25 - 1)

a = [0] * (t + 1)

for i in range(t + 1):
    a[t - i] = N%26
    N = N //26

#print(a)

for i in range(0, len(a)):
    a[i] = chr(97+int(a[i]))
    s += a[i]

#s += chr(97+a[len(a)-1])

print(s)
