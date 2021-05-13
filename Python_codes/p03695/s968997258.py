n = int(input())
arr = list(map(int, input().split()))
freq = [False] * 8 + [0]
for i in range(n):
    a = arr[i]
    if a < 400:
        freq[0] = True
    elif a < 800:
        freq[1] = True
    elif a < 1200:
        freq[2] = True
    elif a < 1600:
        freq[3] = True
    elif a < 2000:
        freq[4] = True
    elif a < 2400:
        freq[5] = True
    elif a < 2800:
        freq[6] = True
    elif a < 3200:
        freq[7] = True
    else:
        freq[8] += 1
print (max(freq[0:8].count(True), 1), freq[0:8].count(True)+freq[8])