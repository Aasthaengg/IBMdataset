S = input()
T = input()

count = 0
forecast1 = S[0]
result1 = T[0]

if forecast1 == result1:
    count = count + 1


forecast2 = S[1]
result2 = T[1]

if forecast2 == result2:
    count = count + 1

    
forecast3 = S[2]
result3 = T[2]

if forecast3 == result3:
    count = count + 1

print(count)
