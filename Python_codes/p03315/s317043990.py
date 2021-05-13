S = input()

s1 = S[0]
s2 = S[1]
s3 = S[2]
s4 = S[3]

n = int(0)

if s1 == "+":
    n += 1
elif s1 == "-":
    n -= 1


if s2 == "+":
    n += 1
elif s2 == "-":
    n -= 1

if s3 == "+":
    n += 1
elif s3 =="-":
    n -= 1

if s4 == "+":
    n += 1
elif s4 == "-":
    n -= 1

print(n)