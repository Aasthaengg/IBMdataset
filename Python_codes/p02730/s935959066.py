S = input()
answer = 'Yes'
if S != S[::-1]:
    answer = 'No'
first = S[:len(S) // 2]
last = S[len(S) // 2 + 1:]
if first != first[::-1]:
    answer = 'No'
if last != last[::-1]:
    answer = 'No'
print(answer)