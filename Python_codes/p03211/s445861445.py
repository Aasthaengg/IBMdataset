S = list(input())

dif = float('inf')

for i in range(len(S)-2):
    num = S[i:i+3]
    num = ''.join(num)
    if abs(int(num) - 753) < dif:
        dif = abs(int(num) - 753)
    
print(dif)
