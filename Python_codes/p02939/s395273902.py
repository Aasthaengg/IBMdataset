S = list(str(input()))
i=1
count = 0

while i < len(S):
    if S[i] == S[i-1]:
        count += 1 #本来増分が0の数をカウント
        i += 2
    i += 1
 
print(len(S)-count)