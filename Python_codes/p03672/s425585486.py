S = input()

index = len(S)-2

while index>0:
    half = index // 2
    if S[:half] == S[half:index]:
        break
    index -= 2

print(index)