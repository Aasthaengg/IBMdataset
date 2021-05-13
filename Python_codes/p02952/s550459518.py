n = int(input())
strDigits = [str(i) for i in range(1,n+1)]
oddCount = 0
for i in range(len(strDigits)):
    if len(strDigits[i]) % 2 == 1:
        oddCount += 1
print(oddCount)