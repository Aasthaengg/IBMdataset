S = input()
count = 1
i = 0
initial_length = len(S)-1
l = S[0]
S = S + '&' + '%'
while i < initial_length:
    if l == S[i+1]:
        if i == initial_length-1:
            break
        elif S[i+2] == S[i+3]:
            l = S[i+3]
            i += 3
            count += 1
        else:
            l = S[i+1:i+3]
            i += 2
    else:
        l = S[i+1]
        i += 1
    count += 1
print(count)