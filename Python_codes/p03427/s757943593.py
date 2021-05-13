# A - Digit Sum 2

N = input()
digit = len(N)
ans = 0

for i in range(digit):
    ans += int(N[i])
    if i<digit-1 and N[i+1]!='9':
        ans += 9*(digit-1-i)-1
        break

print(ans)